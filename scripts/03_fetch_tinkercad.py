"""
03_fetch_tinkercad.py
---------------------
Fetches designs from Tinkercad using Playwright browser automation.

Since Tinkercad has no public bulk-export API, this script:
  1. Logs in with credentials entered at runtime (never written to disk)
  2. Scrapes the designs gallery for metadata
  3. Triggers .stl export downloads for each design

Outputs per design (under 3d-files/tinkercad/{design_id}/):
  metadata.json   — name, description, date, URL
  files/          — exported .stl files

FALLBACK: If automation is blocked, the script writes:
  3d-files/tinkercad/TODO.md  — checklist of all design URLs for manual export

Usage:
  python 03_fetch_tinkercad.py [--dry-run] [--list-only]

Options:
  --dry-run      Print actions without writing files or logging in
  --list-only    Only scrape metadata (no file downloads, no login needed for public profiles)
"""

import argparse
import getpass
import json
import sys
import time
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
CONFIG_PATH = SCRIPT_DIR / "config.yaml"
STATE_PATH = SCRIPT_DIR / "state_tinkercad.json"

TINKERCAD_BASE = "https://www.tinkercad.com"

def load_config():
    if not CONFIG_PATH.exists():
        sys.exit("ERROR: config.yaml not found. Copy config.yaml.example and fill in credentials.")
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)

def load_state():
    if STATE_PATH.exists():
        with open(STATE_PATH) as f:
            return json.load(f)
    return {"completed_designs": []}

def save_state(state):
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)

def ensure_playwright():
    try:
        from playwright.sync_api import sync_playwright
        return sync_playwright
    except ImportError:
        sys.exit("ERROR: Playwright not installed. Run: pip install playwright && playwright install chromium")

# ── Scraping helpers ──────────────────────────────────────────────────────────

def scrape_designs_public(page, user_id):
    """Scrape design metadata from the public profile page (no login needed)."""
    url = f"{TINKERCAD_BASE}/users/{user_id}/designs"
    page.goto(url, wait_until="networkidle")
    time.sleep(2)

    # Scroll to load all designs (infinite scroll)
    prev_count = 0
    while True:
        page.keyboard.press("End")
        time.sleep(1.5)
        cards = page.query_selector_all("[data-design-id]")
        if len(cards) == prev_count:
            break
        prev_count = len(cards)

    designs = []
    for card in page.query_selector_all("[data-design-id]"):
        design_id = card.get_attribute("data-design-id")
        name_el = card.query_selector("[class*='name'], [class*='title'], h3, h4")
        name = name_el.inner_text().strip() if name_el else "Unknown"
        link_el = card.query_selector("a[href]")
        href = link_el.get_attribute("href") if link_el else ""
        full_url = f"{TINKERCAD_BASE}{href}" if href.startswith("/") else href
        designs.append({
            "design_id": design_id,
            "name": name,
            "url": full_url,
        })
    return designs

def login_tinkercad(page, email, password):
    """Log in to Tinkercad using Autodesk credentials."""
    page.goto(f"{TINKERCAD_BASE}/login", wait_until="networkidle")
    time.sleep(1)

    # Tinkercad uses Autodesk login flow
    signin_btn = page.query_selector("button[data-testid='signin-button'], a[href*='login'], button:has-text('Sign In')")
    if signin_btn:
        signin_btn.click()
        time.sleep(2)

    page.fill("input[type='email'], input[name='email'], #userName", email)
    page.keyboard.press("Enter")
    time.sleep(1)

    page.fill("input[type='password'], input[name='password'], #password", password)
    page.keyboard.press("Enter")
    time.sleep(3)

    # Verify login succeeded
    if "login" in page.url.lower() or "signin" in page.url.lower():
        raise RuntimeError("Login failed — check credentials")
    print("  Logged in successfully")

def export_design_stl(page, design_url, out_dir):
    """Navigate to a design and trigger STL export download."""
    page.goto(design_url, wait_until="networkidle")
    time.sleep(2)

    # Look for Export button
    export_btn = page.query_selector("button:has-text('Export'), [aria-label*='Export']")
    if not export_btn:
        print(f"    WARNING: No export button found at {design_url}")
        return False

    export_btn.click()
    time.sleep(1)

    # Select STL option
    stl_option = page.query_selector("button:has-text('.STL'), [data-format='stl'], li:has-text('STL')")
    if not stl_option:
        print(f"    WARNING: No STL option found")
        return False

    # Set download path and trigger
    with page.expect_download() as download_info:
        stl_option.click()
    download = download_info.value
    dest = out_dir / download.suggested_filename
    download.save_as(dest)
    return True

# ── Fallback: generate TODO.md ────────────────────────────────────────────────

def write_todo_fallback(designs, base_dir):
    todo_path = base_dir / "3d-files" / "tinkercad" / "TODO.md"
    todo_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Tinkercad Manual Export Checklist",
        "",
        "Automated export was not possible. Please export each design manually:",
        "1. Open the design URL",
        "2. Click **Export** → **Download for 3D Printing** → **.STL**",
        "3. Save the file to `3d-files/tinkercad/{design_id}/files/`",
        "",
        "## Designs",
        "",
    ]
    for d in designs:
        lines.append(f"- [ ] **{d['name']}** — [{d['url']}]({d['url']})")
        lines.append(f"  - Save to: `3d-files/tinkercad/{d['design_id']}/files/`")
    with open(todo_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  Wrote manual export checklist to {todo_path}")

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Fetch Tinkercad designs via browser automation")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--list-only", action="store_true",
                        help="Scrape metadata only (no file downloads)")
    args = parser.parse_args()

    config = load_config()
    state = load_state()
    user_id = config["tinkercad"]["user_id"]

    base_dir = REPO_ROOT / config.get("output", {}).get("base_dir", ".")
    base_dir = base_dir.resolve()

    sync_playwright = ensure_playwright()

    if args.dry_run:
        print(f"[dry-run] Would fetch Tinkercad designs for user: {user_id}")
        return

    print(f"Fetching Tinkercad designs for: {user_id}")
    print(f"  Profile URL: https://www.tinkercad.com/users/{user_id}/designs")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not args.list_only)
        context = browser.new_context()

        if not args.list_only:
            # Set default download path
            context = p.chromium.launch(headless=False).new_context(
                accept_downloads=True
            )

        page = context.new_page()

        # Step 1: Scrape public profile for design list
        print("  Scraping design list from public profile...")
        try:
            designs = scrape_designs_public(page, user_id)
            print(f"  Found {len(designs)} designs")
        except Exception as e:
            print(f"  ERROR scraping profile: {e}")
            print("  Falling back to empty list. Please provide design URLs manually.")
            designs = []

        # Write metadata for each design
        for design in designs:
            did = design["design_id"]
            out_dir = base_dir / "3d-files" / "tinkercad" / did
            out_dir.mkdir(parents=True, exist_ok=True)
            files_dir = out_dir / "files"
            files_dir.mkdir(exist_ok=True)
            meta_path = out_dir / "metadata.json"
            if not meta_path.exists():
                with open(meta_path, "w", encoding="utf-8") as f:
                    json.dump(design, f, indent=2, ensure_ascii=False)

        if args.list_only:
            print("  List-only mode: skipping file downloads")
            write_todo_fallback(designs, base_dir)
            browser.close()
            return

        # Step 2: Login for downloads
        email = input("Tinkercad/Autodesk email: ")
        password = getpass.getpass("Tinkercad/Autodesk password: ")

        try:
            login_tinkercad(page, email, password)
        except Exception as e:
            print(f"  ERROR: Login failed: {e}")
            print("  Generating manual export checklist instead...")
            write_todo_fallback(designs, base_dir)
            browser.close()
            return

        # Step 3: Export each design
        pending = [d for d in designs if d["design_id"] not in state["completed_designs"]]
        print(f"  {len(designs) - len(pending)} already done, {len(pending)} remaining")

        for design in pending:
            did = design["design_id"]
            files_dir = base_dir / "3d-files" / "tinkercad" / did / "files"
            files_dir.mkdir(parents=True, exist_ok=True)
            print(f"  Exporting: {design['name']} ({did})")
            try:
                success = export_design_stl(page, design["url"], files_dir)
                if success:
                    state["completed_designs"].append(did)
                    save_state(state)
            except Exception as e:
                print(f"    ERROR: {e}")
                continue

        browser.close()

    # If some designs failed, write a TODO for the remainder
    failed = [d for d in designs if d["design_id"] not in state["completed_designs"]]
    if failed:
        write_todo_fallback(failed, base_dir)

    print("\nDone. Run 04_summarize.py next.")

if __name__ == "__main__":
    main()
