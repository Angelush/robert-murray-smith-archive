# Archive Build Status

> Last updated: 2026-03-24

This document tracks what has been collected, what is pending, known problems encountered during the initial build, and recommended next steps.

---

## Progress Summary

### Step 01 — YouTube (metadata, transcripts, comments)

| Channel | Videos | Metadata | Comments | Transcripts |
|---------|--------|----------|----------|-------------|
| @ThinkingandTinkering | 2,122 | ✅ | ✅ | ⚠️ ~15 real, rest blocked |
| @TnTtalktime | 83 | ✅ | ✅ | ⚠️ ~22 real, rest blocked |
| @TnTOmnibus | 56 | ✅ | ✅ | ⚠️ rest blocked |
| **Total** | **2,261** | ✅ | ✅ | **37 / 2,261** |

Metadata and comments are fully archived. Transcripts are the outstanding item (see Known Problems below).

### Step 02 — Thingiverse

| Item | Status |
|------|--------|
| Things discovered | 181 |
| Metadata fetched | ✅ 181 / 181 |
| STL / 3D files downloaded | ✅ Complete |
| YouTube cross-references extracted | ✅ (from descriptions) |

### Step 03 — Tinkercad

| Item | Status |
|------|--------|
| Designs | ⏳ Not started |
| Reason | Requires interactive Autodesk/Tinkercad login |

### Step 04 — AI Summaries

| Item | Status |
|------|--------|
| Summaries generated | 0 / 2,261 |
| Reason | Anthropic API account out of credits |

### Step 05 — JSON Indexes

| Item | Status |
|------|--------|
| Indexes built | ⏳ Not yet |
| Reason | Waiting for transcripts + summaries to be complete first |

### Step 06 — Navigation Catalog

| Item | Status |
|------|--------|
| CATALOG.md generated | ⏳ Not yet |
| Reason | Waiting for indexes (Step 05) to be complete first |

---

## Known Problems & Fixes Applied

### 1. youtube_transcript_api v1.x breaking change

**Problem:** The library updated to v1.x, which removed `YouTubeTranscriptApi.get_transcript()` as a class method. All transcript fetches silently failed, writing `NO_TRANSCRIPT_AVAILABLE` to every file.

**Fix applied:** Updated `01_fetch_youtube.py` and `refetch_transcripts.py` to use the new instance-based API:
```python
# Old (broken in v1.x)
YouTubeTranscriptApi.get_transcript(video_id)

# New (v1.x)
YouTubeTranscriptApi().fetch(video_id)
```
Also updated `format_transcript_text()` to use attribute access (`.text`, `.start`) instead of dict access, compatible with both v0.x and v1.x.

### 2. State file skips channels on resume

**Problem:** `01_fetch_youtube.py` marks entire channels as complete in `state_youtube.json`. When re-run, it skips those channels entirely — even if individual files (e.g. transcripts) are missing within them.

**Fix applied:** Created `scripts/refetch_transcripts.py` — a standalone script that scans all video directories directly for missing transcripts, bypassing the state file entirely. Safe to re-run multiple times.

### 3. YouTube IP block on transcript fetching

**Problem:** After fetching ~37 transcripts rapidly, YouTube blocked the IP with an `IpBlocked` error. The remaining 2,224 videos have `NO_TRANSCRIPT_AVAILABLE` as a result.

**Status:** Fixed — multi-cookie rotation now supported.

**Fix applied:** `refetch_transcripts.py` now:
- Auto-discovers all `cookies-*.txt` files in the scripts directory (e.g. `cookies-Account1.txt`, `cookies-Account2.txt`)
- Splits videos evenly across accounts to distribute the load
- If one account gets IP-blocked, remaining videos are handed to the next account
- Distinguishes "genuinely no transcript" (`NO_TRANSCRIPT_AVAILABLE`) from "blocked" (`BLOCKED_RETRY_LATER`)
- Blocked videos are automatically retried on the next run
- Includes configurable delay between requests (`--delay`, default 2s)

**Usage:**
```bash
python scripts/refetch_transcripts.py              # uses all cookies-*.txt files, 2s delay
python scripts/refetch_transcripts.py --delay 3    # slower pace
```

### 4. Anthropic API credits exhausted

**Problem:** The summarizer (`04_summarize.py`) returned a 400 error: "credit balance too low". No summaries were generated.

**Status:** Fixed — CLI backend added (uses Claude Pro subscription, no API credits needed).

**Fix applied:** `04_summarize.py` now supports two backends:
- `--backend cli` (default): Uses the `claude` CLI, which runs on your Claude Pro subscription. No API key or credits needed.
- `--backend api`: Uses the Anthropic Python SDK (original behavior, requires API credits).

**Usage:**
```bash
python scripts/04_summarize.py                    # uses claude CLI + Claude Pro (default)
python scripts/04_summarize.py --backend api      # uses Anthropic API credits
python scripts/04_summarize.py --model claude-opus-4-6 --delay 5   # explicit model + pacing
python scripts/04_summarize.py --video-id ABC123  # test on a single video first
```

### 5. Wrong output path in refetch_transcripts.py (fixed)

**Problem:** Initial version used `Path(__file__).parent.parent / "youtube"` which resolved to `robert-murray-smith-archive/youtube/` — a directory that doesn't exist. The actual output goes to `Rob/youtube/` (one level higher, per `base_dir: ".."` in config).

**Fix applied:** Script now reads `config.yaml` to resolve `base_dir` correctly, matching the behaviour of all other pipeline scripts.

### 6. Repo restructure — flattened directory layout

**Problem:** The project originally lived inside a `robert-murray-smith-archive/` wrapper directory, requiring all paths to navigate up one level (`base_dir: ".."` in config).

**Fix applied:** Repository restructured so all content sits at the root level (`Rob/`). As part of this:
- `config.yaml` updated: `base_dir` changed from `".."` to `"."` — all scripts now resolve paths relative to the repo root directly.
- Cookie files (`cookies-*.txt`) added to `.gitignore` to prevent accidental credential commits.
- `AI_GUIDE.md` added at the repo root to give AI models context about the project structure and conventions.
- `06_build_navigation.py` added to generate `CATALOG.md` — a human- and AI-readable navigation index of all archived content.
- `run_summarize.bat` updated to run `06_build_navigation.py` as a third step after `05_build_indexes.py`.

---

## Recommended Next Steps

In priority order:

### 1. Fix transcripts (IP block) — do first
- Cookie files already in place (`cookies-Account1.txt`, `cookies-Account2.txt`)
- Run: `python scripts/refetch_transcripts.py`
- The script auto-discovers cookie files, splits work evenly, and rotates on block
- Default 2s delay between requests; increase with `--delay 3` if needed

### 2. Generate AI summaries — do after transcripts
- Uses Claude Pro subscription via the `claude` CLI (no API credits needed)
- Run: `python scripts/04_summarize.py`
- Default model: claude-opus-4-6, 5s delay between calls
- Test on one video first: `python scripts/04_summarize.py --video-id <ID>`

### 3. Tinkercad designs
- Run: `python scripts/03_fetch_tinkercad.py`
- You will be prompted for your Autodesk email and password at runtime (never stored)
- If login automation fails, the script generates a `TODO.md` checklist for manual export

### 4. Build indexes and navigation — do last
- Only after transcripts, summaries, and 3D files are complete:
```bash
python scripts/05_build_indexes.py
python scripts/06_build_navigation.py
```
- `05_build_indexes.py` builds `index.json`, per-channel indexes, and all cross-references between 3D models and videos
- `06_build_navigation.py` generates `CATALOG.md` for human and AI browsing
- Or run both in sequence via: `run_summarize.bat`

### 5. Push to GitHub
- Create a repo on GitHub (suggested name: `robert-murray-smith-archive`)
- Note: 3D files (STLs) may exceed GitHub's 100MB file limit — consider enabling **Git LFS** for `*.stl`, `*.3mf`, `*.obj` before pushing:
```bash
git lfs install
git lfs track "*.stl" "*.3mf" "*.obj"
git add .gitattributes
```

---

## File Counts (as of 2026-03-19)

```
youtube/
  @ThinkingandTinkering/  — 2,122 video directories
  @TnTtalktime/           — 83 video directories
  @TnTOmnibus/            — 56 video directories
  Total videos:           2,261
  With real transcripts:  37
  With summaries:         0

3d-files/
  thingiverse/            — 181 thing directories (STLs downloaded)
  tinkercad/              — 0 (not yet fetched)
```

---

## Pipeline Quick Reference

```bash
# Re-fetch missing transcripts (auto-discovers cookies-*.txt files)
python scripts/refetch_transcripts.py

# Generate AI summaries (uses Claude Pro via claude CLI by default)
python scripts/04_summarize.py

# Tinkercad (interactive login required)
python scripts/03_fetch_tinkercad.py

# Build all JSON indexes (run after transcripts + summaries)
python scripts/05_build_indexes.py

# Build navigation catalog / CATALOG.md (run after indexes)
python scripts/06_build_navigation.py

# Full pipeline from scratch (skips already-done items)
python scripts/run_all.py --skip-tinkercad
```
