"""
04_summarize.py
---------------
Generates structured AI summaries for each video using Claude.

Supports two backends:
  - cli (default): Uses the `claude` CLI (Claude Pro subscription, no API credits needed)
  - api: Uses the Anthropic Python SDK (requires API key and credits)

For every video that has a transcript but no summary.md yet, this script:
  1. Reads transcript.txt and comments.json
  2. Calls Claude to produce a structured summary
  3. Saves the result as summary.md

The summary format is designed to be useful for both human reading and AI
retrieval (RAG systems). Each summary includes:
  - Overview
  - Key Topics
  - Materials / Chemicals Mentioned
  - Techniques and Methods
  - Notable Timestamps
  - Robert's Own Comment Replies (from comments.json)

Usage:
  python 04_summarize.py [--channel HANDLE] [--video-id ID] [--dry-run]
  python 04_summarize.py --backend cli          # uses Claude Pro (default)
  python 04_summarize.py --backend api          # uses Anthropic API credits

Options:
  --backend cli|api    Backend to use (default: cli)
  --channel HANDLE     Process only videos in this channel
  --video-id ID        Process only this single video ID
  --model MODEL        Override model name (default: claude-opus-4-6)
  --delay SECONDS      Seconds between API calls (default: 5.0)
  --dry-run            Print what would be sent to Claude without calling API
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

import yaml
from tqdm import tqdm

try:
    import anthropic
except ImportError:
    anthropic = None

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
CONFIG_PATH = SCRIPT_DIR / "config.yaml"

SUMMARY_PROMPT = """\
You are archiving content from Robert Murray-Smith, a beloved British scientist, inventor,
and science communicator. Your task is to produce a structured summary of one of his YouTube
videos, based on the transcript and (optionally) his own replies in the comments.

The summary will be stored in a fan archive repository and used by:
- Fans and followers who want to quickly understand what a video covers
- AI agents performing retrieval over his entire body of work

Produce a summary in the following markdown format EXACTLY:

## Overview
[2–3 sentences describing what the video is about and its main conclusion or takeaway]

## Key Topics
[Bulleted list of the main subjects covered]

## Materials and Chemicals Mentioned
[Bulleted list of specific materials, chemicals, or compounds discussed, with brief context.
 If none, write "None mentioned."]

## Techniques and Methods
[Bulleted list of experimental or fabrication techniques described]

## Notable Timestamps
[Bulleted list of key moments with approximate timestamps from the transcript.
 Format: `[MM:SS]` — description. If transcript has no timestamps, write "Not available."]

## Robert's Own Replies
[If the author comments section below contains replies from Robert himself, summarize the
 key points he added. These are often important clarifications or follow-up insights.
 If none, write "No author replies found."]

---

VIDEO TITLE: {title}
VIDEO URL: {url}
PUBLISHED: {published_at}

TRANSCRIPT:
{transcript}

AUTHOR COMMENTS (replies posted by Robert in the comments):
{author_comments}
"""

def load_config():
    if not CONFIG_PATH.exists():
        sys.exit("ERROR: config.yaml not found. Copy config.yaml.example and fill in credentials.")
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)

def get_author_comments(comments_path, channel_title):
    """Extract comments/replies posted by the video author themselves."""
    if not comments_path.exists():
        return ""
    with open(comments_path, encoding="utf-8") as f:
        comments = json.load(f)

    author_lines = []
    for comment in comments:
        if channel_title and channel_title.lower() in (comment.get("author") or "").lower():
            author_lines.append(f"[Top-level] {comment['text']}")
        for reply in comment.get("replies", []):
            if channel_title and channel_title.lower() in (reply.get("author") or "").lower():
                author_lines.append(f"[Reply] {reply['text']}")

    return "\n\n".join(author_lines) if author_lines else "None"

def truncate_transcript(transcript_text, max_chars=80000):
    """Truncate transcript to fit within context limits, keeping start and end."""
    if len(transcript_text) <= max_chars:
        return transcript_text
    half = max_chars // 2
    return (
        transcript_text[:half]
        + "\n\n[... transcript truncated for length ...]\n\n"
        + transcript_text[-half:]
    )

def generate_summary_cli(prompt, model, timeout=300):
    """Generate summary using the claude CLI (uses Claude Pro subscription)."""
    cmd = ["claude", "-p", "--model", model]
    # Remove all Claude Code env vars to allow running from within a Claude Code session
    env = {k: v for k, v in os.environ.items()
           if k != "CLAUDECODE" and not k.startswith("CLAUDE_CODE_")}
    # Force UTF-8 encoding for subprocess I/O
    env["PYTHONUTF8"] = "1"
    try:
        result = subprocess.run(
            cmd,
            input=prompt,
            capture_output=True,
            text=True,
            timeout=timeout,
            env=env,
            encoding="utf-8",
        )
    except FileNotFoundError:
        sys.exit(
            "ERROR: 'claude' CLI not found in PATH.\n"
            "Install it or use --backend api with an Anthropic API key."
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"claude CLI timed out after {timeout}s")

    if result.returncode != 0:
        # CLI errors often go to stdout, not stderr
        error_detail = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(f"claude CLI failed (exit {result.returncode}): {error_detail[:300]}")

    return result.stdout.strip()


def generate_summary_api(client, model, max_tokens, prompt):
    """Generate summary using the Anthropic Python SDK (requires API credits)."""
    message = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def build_prompt(title, url, published_at, transcript_text, author_comments):
    return SUMMARY_PROMPT.format(
        title=title,
        url=url,
        published_at=published_at or "Unknown",
        transcript=truncate_transcript(transcript_text),
        author_comments=author_comments or "None",
    )


def process_video_dir(video_dir, channel_title, backend, client, model, max_tokens, delay, dry_run=False):
    transcript_path = video_dir / "transcript.txt"
    summary_path = video_dir / "summary.md"
    metadata_path = video_dir / "metadata.json"
    comments_path = video_dir / "comments.json"

    if summary_path.exists():
        return "skipped"

    if not transcript_path.exists():
        return "no_transcript"

    transcript_text = transcript_path.read_text(encoding="utf-8")
    if transcript_text.strip() in ("NO_TRANSCRIPT_AVAILABLE", "BLOCKED_RETRY_LATER"):
        return "no_transcript"

    metadata = {}
    if metadata_path.exists():
        with open(metadata_path, encoding="utf-8") as f:
            metadata = json.load(f)

    author_comments = get_author_comments(comments_path, channel_title or metadata.get("channel_title", ""))

    if dry_run:
        print(f"  [dry-run] Would summarize: {metadata.get('title', video_dir.name)}")
        return "dry_run"

    prompt = build_prompt(
        title=metadata.get("title", video_dir.name),
        url=metadata.get("url", ""),
        published_at=metadata.get("published_at", ""),
        transcript_text=transcript_text,
        author_comments=author_comments,
    )

    try:
        if backend == "cli":
            summary_text = generate_summary_cli(prompt, model)
        else:
            summary_text = generate_summary_api(client, model, max_tokens, prompt)

        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(summary_text)
        return "ok"
    except Exception as e:
        print(f"\n  ERROR summarizing {video_dir.name}: {e}")
        return "error"


def main():
    parser = argparse.ArgumentParser(description="Generate Claude summaries for all videos")
    parser.add_argument("--backend", choices=["cli", "api"], default="cli",
                        help="Backend: 'cli' uses Claude Pro via claude CLI (default), 'api' uses Anthropic SDK")
    parser.add_argument("--channel", help="Process only this channel handle")
    parser.add_argument("--video-id", help="Process only this video ID")
    parser.add_argument("--model", help="Override model name")
    parser.add_argument("--delay", type=float, default=5.0, help="Seconds between calls (default: 5.0)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    config = load_config()
    anthropic_cfg = config.get("anthropic", {})
    model = args.model or anthropic_cfg.get("model", "claude-opus-4-6")
    max_tokens = anthropic_cfg.get("summary_max_tokens", 1500)

    base_dir = REPO_ROOT / config.get("output", {}).get("base_dir", ".")
    base_dir = base_dir.resolve()
    youtube_dir = base_dir / "youtube"

    # Validate backend requirements
    client = None
    if args.backend == "cli":
        if not args.dry_run and not shutil.which("claude"):
            sys.exit("ERROR: 'claude' CLI not found in PATH.\n"
                     "Install it or use --backend api with an Anthropic API key.")
        print(f"Backend: claude CLI (model: {model})")
    elif args.backend == "api":
        if anthropic is None:
            sys.exit("ERROR: 'anthropic' package not installed. Run: pip install anthropic")
        api_key = anthropic_cfg.get("api_key")
        if not api_key:
            sys.exit("ERROR: anthropic.api_key not set in config.yaml (required for --backend api)")
        if not args.dry_run:
            client = anthropic.Anthropic(api_key=api_key)
        print(f"Backend: Anthropic API (model: {model})")

    # Collect all video directories to process
    video_dirs = []

    if args.video_id:
        channel_handle = args.channel or config["youtube"]["channels"][0]["handle"]
        vid_dir = youtube_dir / channel_handle / args.video_id
        if vid_dir.exists():
            video_dirs.append((vid_dir, channel_handle))
        else:
            sys.exit(f"Video directory not found: {vid_dir}")
    else:
        channels = config["youtube"]["channels"]
        if args.channel:
            channels = [c for c in channels if c["handle"] == args.channel]
        for ch in channels:
            handle = ch["handle"]
            ch_dir = youtube_dir / handle
            if not ch_dir.exists():
                continue
            for vid_dir in ch_dir.iterdir():
                if vid_dir.is_dir() and vid_dir.name != "__pycache__":
                    video_dirs.append((vid_dir, handle))

    print(f"Found {len(video_dirs)} video directories to check")

    counts = {"ok": 0, "skipped": 0, "no_transcript": 0, "error": 0, "dry_run": 0}
    for vid_dir, channel_handle in tqdm(video_dirs, desc="Summarizing", unit="video"):
        result = process_video_dir(vid_dir, channel_handle, args.backend, client, model, max_tokens, args.delay, args.dry_run)
        counts[result] = counts.get(result, 0) + 1
        if result == "ok":
            time.sleep(args.delay)

    print(f"\nResults: {counts['ok']} summarized, {counts['skipped']} skipped (already done), "
          f"{counts['no_transcript']} no transcript, {counts['error']} errors")
    if counts['ok'] > 0 or counts['skipped'] > 0:
        print("Run 05_build_indexes.py next.")


if __name__ == "__main__":
    main()
