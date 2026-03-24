# Robert Murray-Smith — Fan Archive

A community-maintained archive of Robert Murray-Smith's vast body of work: YouTube videos, transcripts, AI-generated summaries, comment discussions, and 3D printing projects.

> **This is an unofficial fan archive, not affiliated with Robert Murray-Smith's estate or family.**
> Its purpose is preservation, reference, and making his work accessible to future learners and AI systems.

---

## Contents

| Section | Description |
|---------|-------------|
| [`youtube/`](./youtube/) | Video metadata, transcripts, AI summaries, and full comment archives |
| [`3d-files/thingiverse/`](./3d-files/thingiverse/) | 3D printing files and metadata from Thingiverse |
| [`index.json`](./index.json) | Master JSON index of all content (for AI retrieval) |
| [`CATALOG.md`](./CATALOG.md) | Human-readable browsable index of all content |
| [`AI_GUIDE.md`](./AI_GUIDE.md) | Guide for AI models querying this archive |
| [`scripts/`](./scripts/) | Python scripts used to build this archive |

---

## Repository Structure

```
(repo root)/
├── index.json                         ← Master index (all platforms)
├── CATALOG.md                         ← Human-readable full index
├── AI_GUIDE.md                        ← Instructions for AI models
├── youtube/
│   ├── index.json                     ← All videos index
│   ├── CATALOG.md
│   └── {channel_handle}/
│       ├── channel.json
│       ├── index.json                 ← Per-channel index
│       ├── CATALOG.md
│       └── {video_id}/
│           ├── metadata.json          ← Title, date, tags, stats, URL
│           ├── transcript.txt         ← Timestamped transcript
│           ├── summary.md             ← AI-generated structured summary
│           └── comments.json          ← All comments and replies
├── 3d-files/
│   └── thingiverse/
│       ├── index.json
│       ├── CATALOG.md
│       └── {thing_id}/
│           ├── metadata.json
│           └── files/                 ← .stl, .3mf, etc.
└── scripts/
    ├── requirements.txt
    ├── config.yaml.example
    ├── 01_fetch_youtube.py
    ├── 02_fetch_thingiverse.py
    ├── 04_summarize.py
    ├── 05_build_indexes.py
    └── run_all.py
```

---

## Browsing the Archive

**For humans:** Open any `CATALOG.md` file — they contain formatted tables of all content at that level of the tree, with links to individual items.

**For AI models:** See [`AI_GUIDE.md`](./AI_GUIDE.md) for a full explanation of the index structure, field definitions, and example query patterns.

---

## Using the JSON Indexes for AI Retrieval

The archive is structured for easy integration with RAG (Retrieval-Augmented Generation) systems:

- **`index.json`** — top-level master index with all items across platforms
- Each item has: `type`, `platform`, `title`, `url`, `tags`, `key_topics`, `materials_mentioned`, `summary_excerpt`, `path`, `related_3d_files`
- Full content lives at the `path` field, relative to repo root

Example query flow for an AI agent:
1. Load `index.json` to find relevant items by topic/material
2. Follow the `path` to load `summary.md` for structured context
3. Load `transcript.txt` for full verbatim content
4. Load `comments.json` to find Robert's own clarifications

---

## Rebuilding the Archive

### Prerequisites

```bash
pip install -r scripts/requirements.txt
playwright install chromium
```

You also need:
- **YouTube Data API v3** key — [console.cloud.google.com](https://console.cloud.google.com)
- **Thingiverse API** key — [thingiverse.com/developers](https://www.thingiverse.com/developers)
- **Anthropic API** key — [console.anthropic.com](https://console.anthropic.com)

### Setup

```bash
cp scripts/config.yaml.example scripts/config.yaml
# Edit config.yaml with your API keys and channel handles
# Set output.base_dir to "." (repo root)
```

### Run

```bash
# Full pipeline
python scripts/run_all.py

# Or step by step:
python scripts/01_fetch_youtube.py       # YouTube metadata, transcripts, comments
python scripts/02_fetch_thingiverse.py   # Thingiverse files
python scripts/04_summarize.py           # AI summaries via Claude
python scripts/05_build_indexes.py       # Build JSON indexes and CATALOG.md files

# Test with a single video first:
python scripts/01_fetch_youtube.py --video-id VIDEO_ID
python scripts/04_summarize.py --video-id VIDEO_ID
```

### Resuming

All scripts checkpoint their progress to `scripts/state_*.json` files.
If interrupted, just re-run the same script — it will skip already-completed items.

### YouTube API Quota Note

The free YouTube Data API tier provides 10,000 units/day. Fetching all comments
for a large channel may require multiple days. The scripts handle this gracefully:
just re-run `01_fetch_youtube.py` each day until all videos are complete.

---

## Video Summary Format

Each `summary.md` is structured for both human reading and AI retrieval:

```markdown
## Overview
[2–3 sentence description]

## Key Topics
- Topic 1
- Topic 2

## Materials and Chemicals Mentioned
- Graphene oxide — used as conductive layer
- ...

## Techniques and Methods
- ...

## Notable Timestamps
- [05:23] — Key demonstration begins
- ...

## Robert's Own Replies
[Extracted from comments where Robert responded to viewers]
```

---

## 3D File Licenses

Most Thingiverse files are published under Creative Commons licenses.
Each `metadata.json` in `3d-files/thingiverse/` includes a `"license"` field
with the exact license for that design. Please respect these licenses when
using or distributing the files.

---

## Current Archive Status

> Last updated: 2026-03-19. See [STATUS.md](./STATUS.md) for full details.

| Component | Status | Count |
|-----------|--------|-------|
| YouTube metadata + comments | ✅ Complete | 2,261 videos |
| YouTube transcripts | ⚠️ Partial — IP blocked | 37 / 2,261 |
| AI summaries (`summary.md`) | ⏳ Pending Anthropic credits | 0 / 2,261 |
| Thingiverse 3D files | ✅ Complete | 181 things |
| JSON indexes | ⏳ Not yet built | — |
| CATALOG.md files | ⏳ Not yet built | — |

---

## Contributing

This is a community archive. If you notice missing videos, incorrect metadata,
or broken links, please open an issue or pull request.

---

*Built with love by fans, for fans. Robert Murray-Smith's curiosity and
generosity in sharing his knowledge inspired many — this archive aims to
ensure his work remains accessible.*
