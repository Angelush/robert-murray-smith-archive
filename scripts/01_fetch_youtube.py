"""
01_fetch_youtube.py
-------------------
Fetches video metadata, transcripts, and all comments (+ replies) for every
video across all configured YouTube channels.

Outputs per video (under youtube/{channel_handle}/{video_id}/):
  metadata.json   — title, description, tags, date, duration, stats, URL
  transcript.txt  — raw auto-generated transcript with timestamps
  comments.json   — all top-level comments and their replies

Progress is checkpointed to scripts/state_youtube.json so the script can be
safely interrupted and resumed (important given YouTube API quota limits).

Usage:
  python 01_fetch_youtube.py [--channel HANDLE] [--video-id ID] [--dry-run]

Options:
  --channel HANDLE   Process only this channel handle (for testing)
  --video-id ID      Process only this single video ID (for testing)
  --dry-run          Print what would be done without writing files
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

import yaml
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from tqdm import tqdm
from youtube_transcript_api import YouTubeTranscriptApi
try:
    from youtube_transcript_api import NoTranscriptFound, TranscriptsDisabled
except ImportError:
    # v1.x moved/renamed these — define fallbacks
    NoTranscriptFound = Exception
    TranscriptsDisabled = Exception

_YT_API = YouTubeTranscriptApi()

# ── Config ────────────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
CONFIG_PATH = SCRIPT_DIR / "config.yaml"
STATE_PATH = SCRIPT_DIR / "state_youtube.json"

def load_config():
    if not CONFIG_PATH.exists():
        sys.exit(f"ERROR: config.yaml not found at {CONFIG_PATH}\n"
                 f"Copy config.yaml.example to config.yaml and fill in your credentials.")
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)

def load_state():
    if STATE_PATH.exists():
        with open(STATE_PATH) as f:
            return json.load(f)
    return {"completed_videos": [], "completed_channels": []}

def save_state(state):
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)

# ── YouTube API helpers ───────────────────────────────────────────────────────

def build_youtube(api_key):
    return build("youtube", "v3", developerKey=api_key)

def get_channel_id(youtube, handle):
    """Resolve a @handle to a channel ID."""
    handle_clean = handle.lstrip("@")
    response = youtube.search().list(
        part="snippet",
        q=handle_clean,
        type="channel",
        maxResults=1
    ).execute()
    items = response.get("items", [])
    if not items:
        raise ValueError(f"Channel not found for handle: {handle}")
    return items[0]["snippet"]["channelId"]

def get_uploads_playlist_id(youtube, channel_id):
    response = youtube.channels().list(
        part="contentDetails",
        id=channel_id
    ).execute()
    return response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

def get_all_video_ids(youtube, playlist_id):
    """Paginate through the uploads playlist to get all video IDs."""
    video_ids = []
    next_page_token = None
    while True:
        response = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()
        for item in response["items"]:
            video_ids.append(item["contentDetails"]["videoId"])
        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break
    return video_ids

def get_video_metadata(youtube, video_id):
    """Fetch full video metadata from the Videos API."""
    response = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=video_id
    ).execute()
    if not response["items"]:
        return None
    item = response["items"][0]
    snippet = item["snippet"]
    stats = item.get("statistics", {})
    return {
        "video_id": video_id,
        "title": snippet.get("title"),
        "description": snippet.get("description"),
        "published_at": snippet.get("publishedAt"),
        "channel_id": snippet.get("channelId"),
        "channel_title": snippet.get("channelTitle"),
        "tags": snippet.get("tags", []),
        "duration": item["contentDetails"].get("duration"),
        "view_count": stats.get("viewCount"),
        "like_count": stats.get("likeCount"),
        "comment_count": stats.get("commentCount"),
        "url": f"https://www.youtube.com/watch?v={video_id}",
        "thumbnail": snippet.get("thumbnails", {}).get("high", {}).get("url"),
    }

def get_transcript(video_id):
    """Fetch transcript text. Returns list of snippet objects (v1.x) or dicts (v0.x)."""
    try:
        return _YT_API.fetch(video_id)
    except Exception:
        return None

def format_transcript_text(transcript):
    """Format transcript into readable timestamped text. Handles both v0.x dicts and v1.x snippet objects."""
    lines = []
    for entry in transcript:
        # v1.x: attribute access; v0.x: dict access
        start = int(getattr(entry, "start", None) or entry.get("start", 0))
        text = getattr(entry, "text", None) or entry.get("text", "")
        minutes, seconds = divmod(start, 60)
        hours, minutes = divmod(minutes, 60)
        if hours:
            ts = f"[{hours:02d}:{minutes:02d}:{seconds:02d}]"
        else:
            ts = f"[{minutes:02d}:{seconds:02d}]"
        lines.append(f"{ts} {text}")
    return "\n".join(lines)

def get_all_comments(youtube, video_id):
    """Fetch all top-level comments and their replies for a video."""
    comments = []
    next_page_token = None
    try:
        while True:
            response = youtube.commentThreads().list(
                part="snippet,replies",
                videoId=video_id,
                maxResults=100,
                pageToken=next_page_token,
                textFormat="plainText"
            ).execute()
            for item in response["items"]:
                top = item["snippet"]["topLevelComment"]["snippet"]
                comment = {
                    "id": item["id"],
                    "author": top.get("authorDisplayName"),
                    "author_channel_id": top.get("authorChannelId", {}).get("value"),
                    "text": top.get("textDisplay"),
                    "likes": top.get("likeCount", 0),
                    "published_at": top.get("publishedAt"),
                    "reply_count": item["snippet"].get("totalReplyCount", 0),
                    "replies": [],
                }
                # Attach replies if present
                if "replies" in item:
                    for reply_item in item["replies"]["comments"]:
                        r = reply_item["snippet"]
                        comment["replies"].append({
                            "id": reply_item["id"],
                            "author": r.get("authorDisplayName"),
                            "author_channel_id": r.get("authorChannelId", {}).get("value"),
                            "text": r.get("textDisplay"),
                            "likes": r.get("likeCount", 0),
                            "published_at": r.get("publishedAt"),
                        })
                comments.append(comment)
            next_page_token = response.get("nextPageToken")
            if not next_page_token:
                break
    except HttpError as e:
        if e.resp.status == 403:
            # Comments disabled on this video
            pass
        else:
            raise
    return comments

# ── API retry wrapper ─────────────────────────────────────────────────────────

def with_retry(fn, retries=5, backoff=2.0):
    for attempt in range(retries):
        try:
            return fn()
        except HttpError as e:
            if e.resp.status in (429, 500, 503):
                wait = backoff ** attempt
                print(f"  Rate limited / server error, retrying in {wait:.0f}s...")
                time.sleep(wait)
            else:
                raise
    raise RuntimeError(f"Failed after {retries} retries")

# ── Per-video processing ──────────────────────────────────────────────────────

def process_video(youtube, video_id, channel_handle, base_dir, dry_run=False):
    out_dir = base_dir / "youtube" / channel_handle / video_id
    if dry_run:
        print(f"  [dry-run] Would write to {out_dir}")
        return

    out_dir.mkdir(parents=True, exist_ok=True)

    # Metadata
    metadata_path = out_dir / "metadata.json"
    if not metadata_path.exists():
        metadata = with_retry(lambda: get_video_metadata(youtube, video_id))
        if metadata:
            with open(metadata_path, "w", encoding="utf-8") as f:
                json.dump(metadata, f, indent=2, ensure_ascii=False)

    # Transcript
    transcript_path = out_dir / "transcript.txt"
    if not transcript_path.exists():
        transcript = get_transcript(video_id)
        if transcript:
            with open(transcript_path, "w", encoding="utf-8") as f:
                f.write(format_transcript_text(transcript))
        else:
            transcript_path.write_text("NO_TRANSCRIPT_AVAILABLE")

    # Comments
    comments_path = out_dir / "comments.json"
    if not comments_path.exists():
        comments = with_retry(lambda: get_all_comments(youtube, video_id))
        with open(comments_path, "w", encoding="utf-8") as f:
            json.dump(comments, f, indent=2, ensure_ascii=False)

# ── Channel processing ────────────────────────────────────────────────────────

def process_channel(youtube, handle, base_dir, state, dry_run=False):
    print(f"\nChannel: {handle}")
    channel_dir = base_dir / "youtube" / handle
    channel_dir.mkdir(parents=True, exist_ok=True)

    channel_id = with_retry(lambda: get_channel_id(youtube, handle))
    playlist_id = with_retry(lambda: get_uploads_playlist_id(youtube, channel_id))

    # Write channel.json
    channel_meta_path = channel_dir / "channel.json"
    if not channel_meta_path.exists() and not dry_run:
        with open(channel_meta_path, "w") as f:
            json.dump({"handle": handle, "channel_id": channel_id,
                       "uploads_playlist_id": playlist_id}, f, indent=2)

    video_ids = with_retry(lambda: get_all_video_ids(youtube, playlist_id))
    print(f"  Found {len(video_ids)} videos")

    pending = [vid for vid in video_ids if vid not in state["completed_videos"]]
    print(f"  {len(state['completed_videos'])} already done, {len(pending)} remaining")

    for video_id in tqdm(pending, desc=f"  {handle}", unit="video"):
        try:
            process_video(youtube, video_id, handle, base_dir, dry_run)
            if not dry_run:
                state["completed_videos"].append(video_id)
                save_state(state)
        except Exception as e:
            print(f"\n  ERROR on {video_id}: {e}")
            continue

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Fetch YouTube data for all configured channels")
    parser.add_argument("--channel", help="Process only this channel handle")
    parser.add_argument("--video-id", help="Process only this single video ID")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without writing files")
    parser.add_argument("--api-key", help="Override the YouTube API key from config (for parallel workers)")
    parser.add_argument("--state-file", help="Override the state file path (for parallel workers)")
    args = parser.parse_args()

    config = load_config()

    global STATE_PATH
    if args.state_file:
        STATE_PATH = Path(args.state_file)

    state = load_state()
    base_dir = REPO_ROOT / config.get("output", {}).get("base_dir", ".")
    base_dir = base_dir.resolve()

    api_key = args.api_key or config["youtube"]["api_key"]
    youtube = build_youtube(api_key)

    # Single video mode (for testing)
    if args.video_id:
        handle = args.channel or config["youtube"]["channels"][0]["handle"]
        print(f"Single video mode: {args.video_id}")
        process_video(youtube, args.video_id, handle, base_dir, args.dry_run)
        return

    channels = config["youtube"]["channels"]
    if args.channel:
        channels = [c for c in channels if c["handle"] == args.channel]
        if not channels:
            sys.exit(f"Channel '{args.channel}' not found in config")

    for channel_cfg in channels:
        handle = channel_cfg["handle"]
        if handle in state["completed_channels"]:
            print(f"Skipping {handle} (already completed)")
            continue
        process_channel(youtube, handle, base_dir, state, args.dry_run)
        if not args.dry_run:
            state["completed_channels"].append(handle)
            save_state(state)

    print("\nDone. Run 04_summarize.py next to generate AI summaries.")

if __name__ == "__main__":
    main()
