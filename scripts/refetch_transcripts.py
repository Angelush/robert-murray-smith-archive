"""
refetch_transcripts.py
----------------------
Re-fetches transcripts for all video directories that are missing a transcript.txt.
Does NOT touch metadata, comments, or the state file.
Safe to run multiple times — skips videos that already have a real transcript.

Uses yt-dlp as the primary backend (much more resilient against YouTube blocks).
Falls back to youtube_transcript_api if yt-dlp fails for a specific video.

Supports multiple cookie files (cookies-Account1.txt, cookies-Account2.txt, etc.)
and rotates between them if one gets blocked.
"""

import argparse
import json
import re
import signal
import sys
import tempfile
import threading
import time
from pathlib import Path

import yaml
import yt_dlp
from tqdm import tqdm

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
with open(SCRIPT_DIR / "config.yaml") as _f:
    _cfg = yaml.safe_load(_f)
BASE_DIR = (REPO_ROOT / _cfg.get("output", {}).get("base_dir", ".")).resolve()
YOUTUBE_DIR = BASE_DIR / "youtube"

_BLOCKED_MARKER = "BLOCKED_RETRY_LATER"


def discover_cookie_files():
    """Find all cookies-*.txt files. Returns list of Path objects."""
    cookie_files = sorted(SCRIPT_DIR.glob("cookies-*.txt"))
    if not cookie_files:
        single = SCRIPT_DIR / "cookies.txt"
        if single.exists():
            cookie_files = [single]
    for cf in cookie_files:
        print(f"  Found cookies: {cf.name}")
    if not cookie_files:
        print("  No cookie files found — running without authentication.")
    return cookie_files


def format_seconds(s):
    """Convert seconds to [MM:SS] or [HH:MM:SS] timestamp."""
    s = int(s)
    minutes, seconds = divmod(s, 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"[{hours:02d}:{minutes:02d}:{seconds:02d}]"
    return f"[{minutes:02d}:{seconds:02d}]"


def fetch_with_ytdlp(video_id, cookie_file=None):
    """Fetch transcript using yt-dlp Python API. Returns formatted text, 'BLOCKED', or None."""
    url = f"https://www.youtube.com/watch?v={video_id}"

    with tempfile.TemporaryDirectory() as tmpdir:
        opts = {
            "skip_download": True,
            "writesubtitles": True,
            "writeautomaticsub": True,
            "subtitleslangs": ["en"],
            "subtitlesformat": "json3",
            "outtmpl": f"{tmpdir}/%(id)s.%(ext)s",
            "quiet": True,
            "no_warnings": True,
            "format": "best",
            "ignore_no_formats_error": True,
            "extractor_args": {"youtube": {"player_client": ["tv"]}},
        }
        if cookie_file:
            opts["cookiefile"] = str(cookie_file)

        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([url])
        except yt_dlp.utils.DownloadError as e:
            msg = str(e).lower()
            if "sign in to confirm" in msg or "bot" in msg or "blocked" in msg or "429" in msg or "too many" in msg:
                return "BLOCKED"
            if "unavailable" in msg or "private" in msg or "removed" in msg:
                return None
            raise

        # Find the subtitle file
        tmppath = Path(tmpdir)
        sub_files = list(tmppath.glob(f"{video_id}*.json3"))

        if not sub_files:
            sub_files = list(tmppath.glob(f"{video_id}*.vtt")) + list(tmppath.glob(f"{video_id}*.srt"))
            if sub_files:
                return _parse_vtt(sub_files[0])
            return None

        return _parse_json3(sub_files[0])


def _parse_json3(filepath):
    """Parse json3 subtitle format into timestamped text."""
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    events = data.get("events", [])
    lines = []
    seen_text = set()

    for event in events:
        # Skip events without segments (e.g., style events)
        segs = event.get("segs")
        if not segs:
            continue

        text = "".join(s.get("utf8", "") for s in segs).strip()
        text = re.sub(r'\s+', ' ', text)

        if not text or text in seen_text or text == "\n":
            continue
        seen_text.add(text)

        start_ms = event.get("tStartMs", 0)
        ts = format_seconds(start_ms / 1000)
        lines.append(f"{ts} {text}")

    return "\n".join(lines) if lines else None


def _parse_vtt(filepath):
    """Parse VTT subtitle format into timestamped text."""
    content = filepath.read_text(encoding="utf-8")
    lines = []
    seen_text = set()

    # Match timestamp lines and following text
    pattern = re.compile(r'(\d{2}):(\d{2}):(\d{2})\.\d+ --> .+\n(.+?)(?:\n|$)')
    for m in pattern.finditer(content):
        h, mn, s, text = m.group(1), m.group(2), m.group(3), m.group(4).strip()
        text = re.sub(r'<[^>]+>', '', text)  # Strip HTML tags
        if not text or text in seen_text:
            continue
        seen_text.add(text)
        total_s = int(h) * 3600 + int(mn) * 60 + int(s)
        ts = format_seconds(total_s)
        lines.append(f"{ts} {text}")

    return "\n".join(lines) if lines else None


def fetch_with_timeout(video_id, cookie_file, timeout_secs=90):
    """Run fetch_with_ytdlp in a thread with a timeout. Returns result or 'TIMEOUT'."""
    result = [None]
    error = [None]

    def _worker():
        try:
            result[0] = fetch_with_ytdlp(video_id, cookie_file)
        except Exception as e:
            error[0] = e

    t = threading.Thread(target=_worker, daemon=True)
    t.start()
    t.join(timeout=timeout_secs)

    if t.is_alive():
        return "TIMEOUT"
    if error[0]:
        raise error[0]
    return result[0]


def main():
    parser = argparse.ArgumentParser(description="Re-fetch missing YouTube transcripts via yt-dlp")
    parser.add_argument("--delay", type=float, default=1.5, help="Seconds between requests (default: 1.5)")
    parser.add_argument("--limit", type=int, default=0, help="Max videos to process (0 = all)")
    parser.add_argument("--timeout", type=int, default=90, help="Per-video timeout in seconds (default: 90)")
    args = parser.parse_args()

    print("Discovering cookie files...")
    cookie_files = discover_cookie_files()
    current_cookie_idx = 0
    print(f"  {len(cookie_files)} account(s) available\n")

    # Collect all video dirs missing a transcript
    missing = []
    for channel_dir in YOUTUBE_DIR.iterdir():
        if not channel_dir.is_dir():
            continue
        for video_dir in channel_dir.iterdir():
            if not video_dir.is_dir():
                continue
            t = video_dir / "transcript.txt"
            if not t.exists():
                missing.append(video_dir)
                continue
            content = t.read_text(encoding="utf-8").strip()
            if content in ("NO_TRANSCRIPT_AVAILABLE", _BLOCKED_MARKER):
                missing.append(video_dir)

    if args.limit > 0:
        missing = missing[:args.limit]

    print(f"Videos to process: {len(missing)}")
    if not missing:
        print("Nothing to do.")
        return

    counts = {"ok": 0, "unavailable": 0, "errors": 0, "blocked": 0, "timeouts": 0}
    consecutive_blocks = 0
    start_time = time.time()

    for i, video_dir in enumerate(missing):
        video_id = video_dir.name
        cookie_file = cookie_files[current_cookie_idx] if cookie_files else None

        # Progress log every 50 videos
        if i > 0 and i % 50 == 0:
            elapsed = time.time() - start_time
            rate = i / elapsed
            eta_min = (len(missing) - i) / rate / 60
            print(f"  [{i}/{len(missing)}] {counts['ok']} fetched, {counts['unavailable']} unavail, "
                  f"{counts['errors']} err, {counts['timeouts']} timeout — ETA {eta_min:.0f}min")

        try:
            result = fetch_with_timeout(video_id, cookie_file, timeout_secs=args.timeout)
        except Exception as e:
            print(f"  Error on {video_id}: {e}")
            counts["errors"] += 1
            time.sleep(args.delay)
            continue

        if result == "TIMEOUT":
            print(f"  Timeout on {video_id} (>{args.timeout}s) — skipping")
            counts["timeouts"] += 1
            time.sleep(args.delay)
            continue

        if result == "BLOCKED":
            consecutive_blocks += 1
            print(f"  Blocked on {video_id} (cookie: {cookie_file.name if cookie_file else 'none'})")

            # Try next cookie file
            if cookie_files and current_cookie_idx < len(cookie_files) - 1:
                current_cookie_idx += 1
                print(f"  Switching to {cookie_files[current_cookie_idx].name}")
                consecutive_blocks = 0
                continue

            if consecutive_blocks >= 5:
                print("  5 consecutive blocks — all accounts exhausted. Stopping.")
                idx = missing.index(video_dir)
                for vd in missing[idx:]:
                    (vd / "transcript.txt").write_text(_BLOCKED_MARKER, encoding="utf-8")
                    counts["blocked"] += 1
                break

            (video_dir / "transcript.txt").write_text(_BLOCKED_MARKER, encoding="utf-8")
            counts["blocked"] += 1

        elif result is None:
            (video_dir / "transcript.txt").write_text("NO_TRANSCRIPT_AVAILABLE", encoding="utf-8")
            counts["unavailable"] += 1
            consecutive_blocks = 0

        else:
            (video_dir / "transcript.txt").write_text(result, encoding="utf-8")
            counts["ok"] += 1
            consecutive_blocks = 0

        time.sleep(args.delay)

    elapsed = time.time() - start_time
    print(f"\nDone in {elapsed/60:.1f} min: {counts['ok']} fetched, {counts['unavailable']} genuinely unavailable, "
          f"{counts['errors']} errors, {counts['timeouts']} timeouts, {counts['blocked']} blocked (will retry next run)")


if __name__ == "__main__":
    main()
