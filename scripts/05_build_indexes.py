"""
05_build_indexes.py
-------------------
Builds JSON indexes at multiple levels for AI retrieval and human navigation.

Indexes created:
  youtube/{channel}/index.json     — all videos for a channel
  youtube/index.json               — all videos across all channels
  3d-files/thingiverse/index.json  — all Thingiverse things
  3d-files/tinkercad/index.json    — all Tinkercad designs
  3d-files/index.json              — all 3D content combined
  index.json                       — master index: everything

Each entry includes a summary_excerpt (first 500 chars of summary.md) for
quick preview without loading the full file.

Usage:
  python 05_build_indexes.py
"""

import json
import re
import sys
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
CONFIG_PATH = SCRIPT_DIR / "config.yaml"

def load_config():
    if not CONFIG_PATH.exists():
        sys.exit("ERROR: config.yaml not found.")
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)

def read_json(path):
    if path.exists():
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return {}

def read_text(path, max_chars=500):
    if path.exists():
        text = path.read_text(encoding="utf-8").strip()
        if text == "NO_TRANSCRIPT_AVAILABLE":
            return None
        return text[:max_chars] + ("..." if len(text) > max_chars else "")
    return None

def extract_topics_from_summary(summary_text):
    """Extract bullet points from the Key Topics section of a summary.md."""
    if not summary_text:
        return []
    match = re.search(r"## Key Topics\n(.*?)(?:\n##|\Z)", summary_text, re.DOTALL)
    if not match:
        return []
    bullets = re.findall(r"[-*]\s+(.+)", match.group(1))
    return [b.strip() for b in bullets]

def extract_materials_from_summary(summary_text):
    """Extract bullet points from the Materials section of a summary.md."""
    if not summary_text:
        return []
    match = re.search(r"## Materials.*?\n(.*?)(?:\n##|\Z)", summary_text, re.DOTALL)
    if not match:
        return []
    bullets = re.findall(r"[-*]\s+(.+)", match.group(1))
    return [b.strip() for b in bullets]

# ── YouTube indexing ──────────────────────────────────────────────────────────

def index_video_dir(video_dir, channel_handle):
    video_id = video_dir.name
    metadata = read_json(video_dir / "metadata.json")
    summary_text = read_text(video_dir / "summary.md", max_chars=600)
    has_transcript = (video_dir / "transcript.txt").exists() and \
                     (video_dir / "transcript.txt").read_text().strip() != "NO_TRANSCRIPT_AVAILABLE"
    comments_path = video_dir / "comments.json"
    comment_count = 0
    if comments_path.exists():
        with open(comments_path, encoding="utf-8") as f:
            comments = json.load(f)
        comment_count = sum(1 + len(c.get("replies", [])) for c in comments)

    summary_full = ""
    summary_path = video_dir / "summary.md"
    if summary_path.exists():
        summary_full = summary_path.read_text(encoding="utf-8")

    return {
        "type": "youtube_video",
        "platform": "youtube",
        "channel": channel_handle,
        "video_id": video_id,
        "title": metadata.get("title"),
        "description": (metadata.get("description") or "")[:300],
        "published_at": metadata.get("published_at"),
        "duration": metadata.get("duration"),
        "tags": metadata.get("tags", []),
        "view_count": metadata.get("view_count"),
        "like_count": metadata.get("like_count"),
        "url": metadata.get("url"),
        "thumbnail": metadata.get("thumbnail"),
        "has_transcript": has_transcript,
        "has_summary": summary_path.exists(),
        "comment_count_archived": comment_count,
        "summary_excerpt": summary_text,
        "key_topics": extract_topics_from_summary(summary_full),
        "materials_mentioned": extract_materials_from_summary(summary_full),
        "path": f"youtube/{channel_handle}/{video_id}",
    }

def build_youtube_indexes(youtube_dir, config):
    all_videos = []
    channels = config["youtube"]["channels"]
    channel_handles = [c["handle"] for c in channels]

    for handle in channel_handles:
        ch_dir = youtube_dir / handle
        if not ch_dir.exists():
            continue

        channel_videos = []
        for video_dir in sorted(ch_dir.iterdir(), key=lambda d: d.name):
            if not video_dir.is_dir() or video_dir.name.startswith("."):
                continue
            if (video_dir / "metadata.json").exists() or (video_dir / "transcript.txt").exists():
                entry = index_video_dir(video_dir, handle)
                channel_videos.append(entry)

        # Sort newest first
        channel_videos.sort(key=lambda v: v.get("published_at") or "", reverse=True)

        # Per-channel index
        ch_index_path = ch_dir / "index.json"
        with open(ch_index_path, "w", encoding="utf-8") as f:
            json.dump({
                "channel": handle,
                "total_videos": len(channel_videos),
                "videos": channel_videos,
            }, f, indent=2, ensure_ascii=False)
        print(f"  youtube/{handle}/index.json — {len(channel_videos)} videos")

        all_videos.extend(channel_videos)

    all_videos.sort(key=lambda v: v.get("published_at") or "", reverse=True)

    # Global YouTube index
    yt_index_path = youtube_dir / "index.json"
    with open(yt_index_path, "w", encoding="utf-8") as f:
        json.dump({
            "total_videos": len(all_videos),
            "channels": channel_handles,
            "videos": all_videos,
        }, f, indent=2, ensure_ascii=False)
    print(f"  youtube/index.json — {len(all_videos)} total videos")

    return all_videos

# ── Thingiverse indexing ──────────────────────────────────────────────────────

def index_thing_dir(thing_dir):
    metadata = read_json(thing_dir / "metadata.json")
    files_dir = thing_dir / "files"
    files = [f.name for f in files_dir.iterdir()] if files_dir.exists() else []
    return {
        "type": "3d_file",
        "platform": "thingiverse",
        "thing_id": thing_dir.name,
        "name": metadata.get("name"),
        "description": (metadata.get("description") or "")[:300],
        "tags": metadata.get("tags", []),
        "categories": metadata.get("categories", []),
        "license": metadata.get("license"),
        "added": metadata.get("added"),
        "url": metadata.get("url"),
        "thumbnail": metadata.get("thumbnail"),
        "like_count": metadata.get("like_count"),
        "download_count": metadata.get("download_count"),
        "file_count": len(files),
        "files": files,
        # related_videos is populated from metadata (YouTube links in description)
        # and enriched with full video titles/paths by build_cross_references()
        "related_videos": metadata.get("related_videos", []),
        "path": f"3d-files/thingiverse/{thing_dir.name}",
    }

def build_thingiverse_index(tv_dir):
    things = []
    for thing_dir in sorted(tv_dir.iterdir(), key=lambda d: d.name):
        if not thing_dir.is_dir() or thing_dir.name.startswith("."):
            continue
        if (thing_dir / "metadata.json").exists():
            things.append(index_thing_dir(thing_dir))

    things.sort(key=lambda t: t.get("added") or "", reverse=True)

    index_path = tv_dir / "index.json"
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump({"total": len(things), "things": things}, f, indent=2, ensure_ascii=False)
    print(f"  3d-files/thingiverse/index.json — {len(things)} things")
    return things

# ── Tinkercad indexing ────────────────────────────────────────────────────────

def index_tinkercad_dir(design_dir):
    metadata = read_json(design_dir / "metadata.json")
    files_dir = design_dir / "files"
    files = [f.name for f in files_dir.iterdir()] if files_dir.exists() else []
    return {
        "type": "3d_file",
        "platform": "tinkercad",
        "design_id": design_dir.name,
        "name": metadata.get("name"),
        "url": metadata.get("url"),
        "file_count": len(files),
        "files": files,
        "path": f"3d-files/tinkercad/{design_dir.name}",
    }

def build_tinkercad_index(tc_dir):
    designs = []
    for design_dir in sorted(tc_dir.iterdir(), key=lambda d: d.name):
        if not design_dir.is_dir() or design_dir.name.startswith("."):
            continue
        if (design_dir / "metadata.json").exists():
            designs.append(index_tinkercad_dir(design_dir))

    index_path = tc_dir / "index.json"
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump({"total": len(designs), "designs": designs}, f, indent=2, ensure_ascii=False)
    print(f"  3d-files/tinkercad/index.json — {len(designs)} designs")
    return designs

# ── Cross-referencing ────────────────────────────────────────────────────────

def build_cross_references(all_youtube, all_thingiverse, all_tinkercad):
    """
    Link 3D models to their corresponding YouTube videos and vice versa.

    For Thingiverse: descriptions contain YouTube URLs which were extracted
    by 02_fetch_thingiverse.py into metadata["related_videos"].
    We enrich those stubs with full video titles, channels, and repo paths.

    For videos: we scan all 3D items to find ones that reference each video,
    and add a "related_3d_files" list to the video entry.
    """
    # Build lookup: video_id → video entry
    video_by_id = {v["video_id"]: v for v in all_youtube if v.get("video_id")}

    # For each Thingiverse thing: enrich related_videos stubs
    for thing in all_thingiverse:
        enriched = []
        for ref in thing.get("related_videos", []):
            vid_id = ref.get("video_id")
            video = video_by_id.get(vid_id)
            if video:
                enriched.append({
                    "video_id": vid_id,
                    "title": video.get("title"),
                    "channel": video.get("channel"),
                    "url": video.get("url"),
                    "published_at": video.get("published_at"),
                    "path": video.get("path"),
                })
            else:
                # Video not in archive yet (different channel, or not yet fetched)
                enriched.append(ref)
        thing["related_videos"] = enriched

    # Tinkercad designs don't have description-based links yet,
    # but we keep the field for future use
    for design in all_tinkercad:
        design.setdefault("related_videos", [])

    # Build reverse lookup: video_id → list of 3D items that reference it
    video_to_3d: dict = {}
    for item in all_thingiverse + all_tinkercad:
        for ref in item.get("related_videos", []):
            vid_id = ref.get("video_id")
            if vid_id:
                video_to_3d.setdefault(vid_id, []).append({
                    "platform": item["platform"],
                    "id": item.get("thing_id") or item.get("design_id"),
                    "name": item.get("name"),
                    "url": item.get("url"),
                    "path": item.get("path"),
                })

    # Attach related_3d_files to each video entry
    for video in all_youtube:
        vid_id = video.get("video_id")
        video["related_3d_files"] = video_to_3d.get(vid_id, [])

    linked_videos = sum(1 for v in all_youtube if v.get("related_3d_files"))
    linked_things = sum(1 for t in all_thingiverse if t.get("related_videos"))
    print(f"  Cross-references: {linked_things} 3D models linked to videos, "
          f"{linked_videos} videos linked to 3D models")

# ── Master index ──────────────────────────────────────────────────────────────

def build_master_index(base_dir, all_youtube, all_thingiverse, all_tinkercad):
    all_items = all_youtube + all_thingiverse + all_tinkercad

    # Combined 3D index
    all_3d = all_thingiverse + all_tinkercad
    with open(base_dir / "3d-files" / "index.json", "w", encoding="utf-8") as f:
        json.dump({"total": len(all_3d), "items": all_3d}, f, indent=2, ensure_ascii=False)
    print(f"  3d-files/index.json — {len(all_3d)} items")

    # Master index
    master = {
        "description": "Robert Murray-Smith Fan Archive — master content index",
        "generated_at": __import__("datetime").datetime.utcnow().isoformat() + "Z",
        "total_items": len(all_items),
        "summary": {
            "youtube_videos": len(all_youtube),
            "thingiverse_things": len(all_thingiverse),
            "tinkercad_designs": len(all_tinkercad),
        },
        "items": all_items,
    }
    with open(base_dir / "index.json", "w", encoding="utf-8") as f:
        json.dump(master, f, indent=2, ensure_ascii=False)
    print(f"  index.json — {len(all_items)} total items")

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    config = load_config()
    base_dir = REPO_ROOT / config.get("output", {}).get("base_dir", ".")
    base_dir = base_dir.resolve()

    youtube_dir = base_dir / "youtube"
    tv_dir = base_dir / "3d-files" / "thingiverse"
    tc_dir = base_dir / "3d-files" / "tinkercad"

    print("Building indexes...")

    all_youtube = build_youtube_indexes(youtube_dir, config) if youtube_dir.exists() else []
    all_thingiverse = build_thingiverse_index(tv_dir) if tv_dir.exists() else []
    all_tinkercad = build_tinkercad_index(tc_dir) if tc_dir.exists() else []

    print("Cross-referencing 3D models with videos...")
    build_cross_references(all_youtube, all_thingiverse, all_tinkercad)

    build_master_index(base_dir, all_youtube, all_thingiverse, all_tinkercad)

    print("\nAll indexes built successfully.")

if __name__ == "__main__":
    main()
