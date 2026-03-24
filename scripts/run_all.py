"""
run_all.py
----------
Orchestrator: runs all five pipeline scripts in sequence.

Each script is run as a subprocess so that failures in one step are isolated.
Progress state files (state_youtube.json, etc.) allow safe resumption.

Usage:
  python run_all.py [--skip-tinkercad] [--skip-summaries] [--dry-run]

Options:
  --skip-tinkercad    Skip Tinkercad (requires browser + login)
  --skip-summaries    Skip Claude summarization (no Anthropic API key needed)
  --dry-run           Pass --dry-run to all scripts
"""

import argparse
import subprocess
import sys
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

STEPS = [
    ("01 — Fetch YouTube data",     "01_fetch_youtube.py"),
    ("02 — Fetch Thingiverse files","02_fetch_thingiverse.py"),
    ("03 — Fetch Tinkercad files",  "03_fetch_tinkercad.py"),
    ("04 — Generate AI summaries",  "04_summarize.py"),
    ("05 — Build JSON indexes",     "05_build_indexes.py"),
]

def run_step(label, script_name, extra_args=None):
    script_path = SCRIPT_DIR / script_name
    cmd = [sys.executable, str(script_path)] + (extra_args or [])
    print(f"\n{'='*60}")
    print(f"  {label}")
    print(f"{'='*60}")
    start = time.time()
    result = subprocess.run(cmd)
    elapsed = time.time() - start
    if result.returncode != 0:
        print(f"\nERROR: {label} failed with exit code {result.returncode}")
        return False
    print(f"\n  Completed in {elapsed:.1f}s")
    return True

def main():
    parser = argparse.ArgumentParser(description="Run the full archive pipeline")
    parser.add_argument("--skip-tinkercad", action="store_true")
    parser.add_argument("--skip-summaries", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    extra = ["--dry-run"] if args.dry_run else []

    skip = set()
    if args.skip_tinkercad:
        skip.add("03_fetch_tinkercad.py")
    if args.skip_summaries:
        skip.add("04_summarize.py")

    print("Robert Murray-Smith Archive Pipeline")
    print(f"Skipping: {skip if skip else 'nothing'}")
    if args.dry_run:
        print("DRY RUN MODE — no files will be written")

    failed = []
    for label, script in STEPS:
        if script in skip:
            print(f"\nSkipping: {label}")
            continue
        success = run_step(label, script, extra)
        if not success:
            failed.append(label)
            print("  Continuing with next step...")

    print(f"\n{'='*60}")
    if failed:
        print(f"Pipeline complete with {len(failed)} error(s):")
        for f in failed:
            print(f"  - {f}")
        print("\nCheck the output above and re-run individual scripts to retry failed steps.")
    else:
        print("Pipeline complete — all steps succeeded.")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
