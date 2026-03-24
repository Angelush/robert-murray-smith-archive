"""
06_build_navigation.py
----------------------
Generates CATALOG.md files for GitHub browsing.

Catalogs created:
  youtube/{channel}/CATALOG.md     — per-channel video table
  3d-files/thingiverse/CATALOG.md  — Thingiverse things table
  CATALOG.md                       — root overview with recent additions

Each catalog is a human-readable markdown file with tables and links designed
for browsing directly on GitHub without cloning the repo.

Usage:
  python 06_build_navigation.py
  python 06_build_navigation.py --dry-run
  python 06_build_navigation.py --channel @ThinkingandTinkering
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml
from tqdm import tqdm

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
CONFIG_PATH = SCRIPT_DIR / "config.yaml"


# ── Config ────────────────────────────────────────────────────────────────────

def load_config():
    if not CONFIG_PATH.exists():
        sys.exit("ERROR: config.yaml not found.")
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


# ── Helpers ───────────────────────────────────────────────────────────────────

def read_json(path):
    if path.exists():
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return {}


def parse_duration(iso_duration):
    """
    Convert ISO 8601 duration string to human-readable format.

    Examples:
      PT3M56S  -> 3:56
      PT1H2M3S -> 1:02:03
      PT45S    -> 0:45
      PT5M     -> 5:00
      PT1H     -> 1:00:00
    """
    if not iso_duration:
        return ""
    match = re.fullmatch(
        r"P(?:(\d+)D)?T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?",
        iso_duration,
    )
    if not match:
        return iso_duration
    days = int(match.group(1) or 0)
    hours = int(match.group(2) or 0) + days * 24
    minutes = int(match.group(3) or 0)
    seconds = int(match.group(4) or 0)

    if hours:
        return f"{hours}:{minutes:02d}:{seconds:02d}"
    return f"{minutes}:{seconds:02d}"


def format_count(n):
    """Format an integer with commas; return empty string for None/falsy."""
    if n is None:
        return ""
    try:
        return f"{int(n):,}"
    except (ValueError, TypeError):
        return str(n)


def format_date(iso_date):
    """Return YYYY-MM-DD from an ISO timestamp, or empty string."""
    if not iso_date:
        return ""
    return str(iso_date)[:10]


def escape_pipe(text):
    """Escape pipe characters so they don't break markdown table cells."""
    if not text:
        return ""
    return str(text).replace("|", "&#124;")


def now_utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


# ── YouTube data loading ───────────────────────────────────────────────────────

def load_channel_videos(channel_dir):
    """
    Read metadata.json directly from each video directory.
    Returns a list of dicts with all fields needed for the catalog.
    """
    videos = []
    for video_dir in sorted(channel_dir.iterdir(), key=lambda d: d.name):
        if not video_dir.is_dir() or video_dir.name.startswith("."):
            continue
        meta_path = video_dir / "metadata.json"
        if not meta_path.exists():
            continue
        meta = read_json(meta_path)
        video_id = video_dir.name
        has_summary = (video_dir / "summary.md").exists()
        transcript_path = video_dir / "transcript.txt"
        has_transcript = (
            transcript_path.exists()
            and transcript_path.read_text(encoding="utf-8").strip()
            != "NO_TRANSCRIPT_AVAILABLE"
        )
        videos.append({
            "video_id": video_id,
            "title": meta.get("title") or video_id,
            "published_at": meta.get("published_at", ""),
            "duration": meta.get("duration", ""),
            "view_count": meta.get("view_count"),
            "url": meta.get("url", ""),
            "has_summary": has_summary,
            "has_transcript": has_transcript,
        })
    videos.sort(key=lambda v: v.get("published_at") or "", reverse=True)
    return videos


# ── YouTube per-channel catalog ────────────────────────────────────────────────

def build_channel_catalog(channel_dir, channel_handle, dry_run=False):
    """Generate youtube/{channel}/CATALOG.md."""
    videos = load_channel_videos(channel_dir)

    total = len(videos)
    total_summaries = sum(1 for v in videos if v["has_summary"])
    total_transcripts = sum(1 for v in videos if v["has_transcript"])

    lines = []
    lines.append(f"# {channel_handle} — Video Catalog\n")
    lines.append(f"_Generated {now_utc()}_\n")
    lines.append(
        f"**{total}** videos archived &nbsp;·&nbsp; "
        f"**{total_summaries}** with AI summaries &nbsp;·&nbsp; "
        f"**{total_transcripts}** with transcripts\n"
    )
    lines.append("")

    # Table header
    lines.append("| Title | Date | Duration | Views | Links |")
    lines.append("|-------|------|----------|-------|-------|")

    for v in videos:
        title = escape_pipe(v["title"])
        date = format_date(v["published_at"])
        duration = parse_duration(v["duration"])
        views = format_count(v["view_count"])

        link_parts = []
        if v["url"]:
            link_parts.append(f"[▶ YouTube]({v['url']})")
        if v["has_summary"]:
            link_parts.append(f"[📋 Summary]({v['video_id']}/summary.md)")
        links = " &nbsp; ".join(link_parts)

        lines.append(f"| {title} | {date} | {duration} | {views} | {links} |")

    content = "\n".join(lines) + "\n"
    out_path = channel_dir / "CATALOG.md"

    if dry_run:
        print(f"  [dry-run] Would write {out_path} ({len(videos)} rows)")
    else:
        out_path.write_text(content, encoding="utf-8")
        print(f"  youtube/{channel_handle}/CATALOG.md — {len(videos)} videos")

    return videos


# ── Thingiverse catalog ────────────────────────────────────────────────────────

def load_thingiverse_things(tv_dir):
    """Read metadata.json directly from each thing directory."""
    things = []
    for thing_dir in sorted(tv_dir.iterdir(), key=lambda d: d.name):
        if not thing_dir.is_dir() or thing_dir.name.startswith("."):
            continue
        meta_path = thing_dir / "metadata.json"
        if not meta_path.exists():
            continue
        meta = read_json(meta_path)
        files_dir = thing_dir / "files"
        file_count = len(list(files_dir.iterdir())) if files_dir.exists() else 0
        things.append({
            "thing_id": thing_dir.name,
            "name": meta.get("name") or thing_dir.name,
            "added": meta.get("added", ""),
            "download_count": meta.get("download_count"),
            "like_count": meta.get("like_count"),
            "file_count": file_count,
            "url": meta.get("url", ""),
            "related_videos": meta.get("related_videos", []),
        })
    things.sort(key=lambda t: t.get("added") or "", reverse=True)
    return things


def build_thingiverse_catalog(tv_dir, dry_run=False):
    """Generate 3d-files/thingiverse/CATALOG.md."""
    things = load_thingiverse_things(tv_dir)

    lines = []
    lines.append("# Thingiverse — Design Catalog\n")
    lines.append(f"_Generated {now_utc()}_\n")
    lines.append(f"**{len(things)}** designs archived\n")
    lines.append("")

    lines.append("| Name | Date Added | Downloads | Likes | Files | Links |")
    lines.append("|------|------------|-----------|-------|-------|-------|")

    for t in things:
        name = escape_pipe(t["name"])
        date = format_date(t["added"])
        downloads = format_count(t["download_count"])
        likes = format_count(t["like_count"])
        files = str(t["file_count"]) if t["file_count"] else ""

        link_parts = []
        if t["url"]:
            link_parts.append(f"[🔗 Thingiverse]({t['url']})")
        for rv in t.get("related_videos", []):
            yt_url = rv.get("url") or rv.get("youtube_url")
            if yt_url:
                link_parts.append(f"[▶ Video]({yt_url})")
        links = " &nbsp; ".join(link_parts)

        lines.append(f"| {name} | {date} | {downloads} | {likes} | {files} | {links} |")

    content = "\n".join(lines) + "\n"
    out_path = tv_dir / "CATALOG.md"

    if dry_run:
        print(f"  [dry-run] Would write {out_path} ({len(things)} rows)")
    else:
        out_path.write_text(content, encoding="utf-8")
        print(f"  3d-files/thingiverse/CATALOG.md — {len(things)} things")

    return things


# ── Root catalog ───────────────────────────────────────────────────────────────

def build_root_catalog(base_dir, all_videos_by_channel, all_things, dry_run=False):
    """Generate root CATALOG.md with overview and recent additions."""
    total_videos = sum(len(v) for v in all_videos_by_channel.values())
    total_summaries = sum(
        sum(1 for v in vids if v["has_summary"])
        for vids in all_videos_by_channel.values()
    )
    total_transcripts = sum(
        sum(1 for v in vids if v["has_transcript"])
        for vids in all_videos_by_channel.values()
    )
    total_things = len(all_things)

    lines = []
    lines.append("# Archive Catalog\n")
    lines.append(f"_Generated {now_utc()}_\n")
    lines.append("## Overview\n")
    lines.append("| Category | Count |")
    lines.append("|----------|-------|")
    lines.append(f"| YouTube videos | {total_videos:,} |")
    lines.append(f"| Videos with AI summaries | {total_summaries:,} |")
    lines.append(f"| Videos with transcripts | {total_transcripts:,} |")
    lines.append(f"| Thingiverse designs | {total_things:,} |")
    lines.append("")

    lines.append("## Sub-Catalogs\n")
    for channel_handle in sorted(all_videos_by_channel.keys()):
        vids = all_videos_by_channel[channel_handle]
        lines.append(
            f"- **[{channel_handle}](youtube/{channel_handle}/CATALOG.md)** "
            f"— {len(vids):,} videos"
        )
    lines.append(
        f"- **[Thingiverse](3d-files/thingiverse/CATALOG.md)** "
        f"— {total_things:,} designs"
    )
    lines.append("")

    # Recent additions — last 50 items across all platforms, sorted by date
    recent_items = []

    for channel_handle, vids in all_videos_by_channel.items():
        for v in vids:
            recent_items.append({
                "platform": "YouTube",
                "name": v["title"],
                "date": format_date(v["published_at"]),
                "link": v["url"],
                "extra": channel_handle,
            })

    for t in all_things:
        recent_items.append({
            "platform": "Thingiverse",
            "name": t["name"],
            "date": format_date(t["added"]),
            "link": t["url"],
            "extra": "",
        })

    recent_items.sort(key=lambda x: x["date"] or "", reverse=True)
    recent_items = recent_items[:50]

    lines.append("## Recent Additions (last 50)\n")
    lines.append("| Date | Platform | Name | Channel / Source |")
    lines.append("|------|----------|------|-----------------|")

    for item in recent_items:
        date = item["date"]
        platform = item["platform"]
        name = escape_pipe(item["name"])
        link = item["link"]
        extra = escape_pipe(item["extra"])
        name_cell = f"[{name}]({link})" if link else name
        lines.append(f"| {date} | {platform} | {name_cell} | {extra} |")

    content = "\n".join(lines) + "\n"
    out_path = base_dir / "CATALOG.md"

    if dry_run:
        print(f"  [dry-run] Would write {out_path} ({len(recent_items)} recent items)")
    else:
        out_path.write_text(content, encoding="utf-8")
        print(f"  CATALOG.md — {total_videos} videos + {total_things} things, "
              f"{len(recent_items)} recent items listed")


# ── Main ──────────────────────────────────────────────────────────────────────

def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate CATALOG.md files for GitHub browsing."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be written without creating any files.",
    )
    parser.add_argument(
        "--channel",
        metavar="HANDLE",
        help="Process only this channel (e.g. @ThinkingandTinkering).",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    config = load_config()
    base_dir = REPO_ROOT / config.get("output", {}).get("base_dir", ".")
    base_dir = base_dir.resolve()

    youtube_dir = base_dir / "youtube"
    tv_dir = base_dir / "3d-files" / "thingiverse"

    channels = config.get("youtube", {}).get("channels", [])
    channel_handles = [c["handle"] for c in channels]

    if args.channel:
        if args.channel not in channel_handles:
            sys.exit(f"ERROR: Channel '{args.channel}' not found in config.yaml.")
        channel_handles = [args.channel]

    print("Building CATALOG.md files...")
    if args.dry_run:
        print("  (dry-run mode — no files will be written)")

    all_videos_by_channel = {}

    # Per-channel catalogs
    for handle in tqdm(channel_handles, desc="YouTube channels", unit="channel"):
        ch_dir = youtube_dir / handle
        if not ch_dir.exists():
            tqdm.write(f"  Skipping {handle} — directory not found")
            continue
        vids = build_channel_catalog(ch_dir, handle, dry_run=args.dry_run)
        all_videos_by_channel[handle] = vids

    # Thingiverse catalog
    all_things = []
    if tv_dir.exists():
        all_things = build_thingiverse_catalog(tv_dir, dry_run=args.dry_run)
    else:
        print("  Skipping Thingiverse — directory not found")

    # Root catalog (only if not filtering to a single channel)
    if not args.channel:
        build_root_catalog(base_dir, all_videos_by_channel, all_things, dry_run=args.dry_run)
    else:
        print("  Skipping root CATALOG.md (single-channel mode)")

    print("\nAll catalogs built successfully.")


if __name__ == "__main__":
    main()
