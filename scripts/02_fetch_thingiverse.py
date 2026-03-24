"""
02_fetch_thingiverse.py
-----------------------
Fetches all "things" published by the configured Thingiverse user, downloads
their files, and saves structured metadata JSON.

Outputs per thing (under 3d-files/thingiverse/{thing_id}/):
  metadata.json   — name, description, tags, license, print settings, date, URL
  files/          — all downloadable files (.stl, .3mf, .obj, etc.)

Usage:
  python 02_fetch_thingiverse.py [--thing-id ID] [--dry-run]

Options:
  --thing-id ID    Process only this single thing ID (for testing)
  --dry-run        Print what would be done without writing files
"""

import argparse
import json
import re
import sys
import time
from pathlib import Path

import requests
import yaml
from tqdm import tqdm

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
CONFIG_PATH = SCRIPT_DIR / "config.yaml"
STATE_PATH = SCRIPT_DIR / "state_thingiverse.json"

THINGIVERSE_API = "https://api.thingiverse.com"

def load_config():
    if not CONFIG_PATH.exists():
        sys.exit(f"ERROR: config.yaml not found. Copy config.yaml.example and fill in credentials.")
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)

def load_state():
    if STATE_PATH.exists():
        with open(STATE_PATH) as f:
            return json.load(f)
    return {"completed_things": []}

def save_state(state):
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)

# ── API helpers ───────────────────────────────────────────────────────────────

def tv_get(endpoint, api_key, params=None, retries=5):
    headers = {"Authorization": f"Bearer {api_key}"}
    url = f"{THINGIVERSE_API}{endpoint}"
    for attempt in range(retries):
        try:
            resp = requests.get(url, headers=headers, params=params, timeout=30)
            if resp.status_code == 429:
                wait = 2 ** attempt
                print(f"  Rate limited, retrying in {wait}s...")
                time.sleep(wait)
                continue
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.RequestException as e:
            if attempt == retries - 1:
                raise
            time.sleep(2 ** attempt)
    raise RuntimeError(f"Failed after {retries} retries: {endpoint}")

def get_user_things(username, api_key):
    """Paginate through all things by a user."""
    things = []
    page = 1
    while True:
        data = tv_get(f"/users/{username}/things", api_key, params={"page": page, "per_page": 30})
        if not data:
            break
        things.extend(data)
        if len(data) < 30:
            break
        page += 1
    return things

def get_thing_detail(thing_id, api_key):
    return tv_get(f"/things/{thing_id}", api_key)

def get_thing_files(thing_id, api_key):
    return tv_get(f"/things/{thing_id}/files", api_key)

def download_file(url, dest_path, api_key, chunk_size=1024 * 64):
    headers = {"Authorization": f"Bearer {api_key}"}
    with requests.get(url, headers=headers, stream=True, timeout=60) as resp:
        resp.raise_for_status()
        with open(dest_path, "wb") as f:
            for chunk in resp.iter_content(chunk_size=chunk_size):
                f.write(chunk)

# ── YouTube URL extraction ────────────────────────────────────────────────────

_YT_URL_RE = re.compile(
    r"https?://(?:www\.)?(?:youtube\.com/watch\?(?:[^&\s]*&)*v=|youtu\.be/)([\w-]{11})"
)

def extract_youtube_urls(text):
    """Extract all YouTube video URLs and their video IDs from a block of text.
    Returns list of {url, video_id} dicts, deduplicated by video_id.
    """
    if not text:
        return []
    seen = {}
    for match in _YT_URL_RE.finditer(text):
        video_id = match.group(1)
        if video_id not in seen:
            seen[video_id] = match.group(0)
    return [{"video_id": vid, "url": url} for vid, url in seen.items()]

# ── Metadata extraction ───────────────────────────────────────────────────────

def build_metadata(detail, files_list):
    description = detail.get("description") or ""
    instructions = detail.get("instructions") or ""
    # Extract YouTube links from both description and instructions
    related_videos = extract_youtube_urls(description + "\n" + instructions)

    return {
        "thing_id": detail.get("id"),
        "name": detail.get("name"),
        "description": description,
        "instructions": instructions,
        "related_videos": related_videos,    # [{video_id, url}] — cross-reference to YouTube
        "tags": [t.get("name") for t in detail.get("tags", [])],
        "categories": [c.get("name") for c in detail.get("categories", [])],
        "license": detail.get("license"),
        "added": detail.get("added"),
        "modified": detail.get("modified"),
        "url": detail.get("public_url"),
        "thumbnail": detail.get("thumbnail"),
        "like_count": detail.get("like_count"),
        "collect_count": detail.get("collect_count"),
        "comment_count": detail.get("comment_count"),
        "download_count": detail.get("download_count"),
        "files": [
            {
                "name": f.get("name"),
                "size": f.get("size"),
                "url": f.get("public_url"),
                "download_url": f.get("download_url"),
            }
            for f in (files_list or [])
        ],
    }

# ── Per-thing processing ──────────────────────────────────────────────────────

def process_thing(thing_id, api_key, base_dir, dry_run=False):
    out_dir = base_dir / "3d-files" / "thingiverse" / str(thing_id)
    files_dir = out_dir / "files"

    if dry_run:
        print(f"  [dry-run] Would write to {out_dir}")
        return

    out_dir.mkdir(parents=True, exist_ok=True)
    files_dir.mkdir(exist_ok=True)

    metadata_path = out_dir / "metadata.json"
    if not metadata_path.exists():
        detail = get_thing_detail(thing_id, api_key)
        files_list = get_thing_files(thing_id, api_key)
        metadata = build_metadata(detail, files_list)
        with open(metadata_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)

        # Download files
        for file_info in (files_list or []):
            file_name = file_info.get("name", f"file_{file_info.get('id')}")
            dest = files_dir / file_name
            if not dest.exists():
                dl_url = file_info.get("download_url") or file_info.get("public_url")
                if dl_url:
                    try:
                        download_file(dl_url, dest, api_key)
                    except Exception as e:
                        print(f"    WARNING: Could not download {file_name}: {e}")

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Fetch Thingiverse things and files")
    parser.add_argument("--thing-id", help="Process only this thing ID (for testing)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    config = load_config()
    state = load_state()
    tv_config = config["thingiverse"]
    api_key = tv_config["api_key"]
    username = tv_config["username"]

    base_dir = REPO_ROOT / config.get("output", {}).get("base_dir", ".")
    base_dir = base_dir.resolve()

    if args.thing_id:
        print(f"Single thing mode: {args.thing_id}")
        process_thing(args.thing_id, api_key, base_dir, args.dry_run)
        return

    print(f"Fetching all things for Thingiverse user: {username}")
    things = get_user_things(username, api_key)
    print(f"Found {len(things)} things")

    pending = [t for t in things if str(t["id"]) not in state["completed_things"]]
    print(f"{len(things) - len(pending)} already done, {len(pending)} remaining")

    for thing in tqdm(pending, desc="Thingiverse", unit="thing"):
        thing_id = str(thing["id"])
        try:
            process_thing(thing_id, api_key, base_dir, args.dry_run)
            if not args.dry_run:
                state["completed_things"].append(thing_id)
                save_state(state)
        except Exception as e:
            print(f"\n  ERROR on thing {thing_id}: {e}")
            continue

    print("\nDone. Run 03_fetch_tinkercad.py next.")

if __name__ == "__main__":
    main()
