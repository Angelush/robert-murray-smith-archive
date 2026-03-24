# Robert Murray-Smith — Fan Archive

A community-maintained archive of Robert Murray-Smith's publicly available YouTube videos: transcripts, AI-generated summaries, comment discussions, and 3D printing project metadata.

> **This is an unofficial fan archive, not affiliated with Robert Murray-Smith's estate or family.**
> Its purpose is preservation, reference, and making his freely available work accessible to future learners and AI systems.
>
> **This archive only contains free, publicly available content.** It does not include any channel-members-only videos, paid content, or private material.

---

## Contents

| Section | Description |
|---------|-------------|
| [`youtube/`](./youtube/) | Video metadata, transcripts, AI summaries, and full comment archives |
| [`3d-files/thingiverse/`](./3d-files/thingiverse/) | 3D printing file metadata from Thingiverse |
| [`index.json`](./index.json) | Master JSON index of all content (for AI retrieval) |
| [`index-compact.json`](./index-compact.json) | Lightweight AI-friendly index (~10x smaller) |
| [`topics.json`](./topics.json) | Topic → video ID lookup for fast search |
| [`CATALOG.md`](./CATALOG.md) | Human-readable browsable index of all content |
| [`AI_GUIDE.md`](./AI_GUIDE.md) | Guide for AI models querying this archive |

---

## Repository Structure

```
(repo root)/
├── index.json                         ← Master index (all platforms)
├── index-compact.json                 ← Lightweight AI-friendly index
├── topics.json                        ← Topic → video ID lookup
├── CATALOG.md                         ← Human-readable full index
├── AI_GUIDE.md                        ← Instructions for AI models
├── youtube/
│   ├── index.json                     ← All videos index
│   ├── CATALOG.md
│   └── {channel_handle}/
│       ├── index.json                 ← Per-channel index
│       ├── CATALOG.md
│       └── {video_id}/
│           ├── README.md              ← Title, link, overview (auto-rendered)
│           ├── metadata.json          ← Title, date, tags, stats, URL
│           ├── transcript.txt         ← Timestamped transcript
│           ├── summary.md             ← AI-generated structured summary
│           └── comments.json          ← All comments and replies
├── 3d-files/
│   └── thingiverse/
│       ├── index.json
│       ├── CATALOG.md
│       └── {thing_id}/
│           ├── README.md              ← Name, link, description (auto-rendered)
│           └── metadata.json
```

---

## Browsing the Archive

**On GitHub:** Navigate into any video folder — the README.md renders automatically with the video title, a clickable YouTube link, and a summary overview. Or open any `CATALOG.md` for formatted tables of all content.

**For AI models:** See [`AI_GUIDE.md`](./AI_GUIDE.md) for index structure, field definitions, and example query patterns.

---

## Using the JSON Indexes for AI Retrieval

The archive is structured for easy integration with RAG (Retrieval-Augmented Generation) systems:

**Start small, go deeper as needed:**

1. **`topics.json`** (~100 KB) — Find video IDs by topic or material name
2. **`index-compact.json`** (~500 KB) — Get metadata for specific videos (title, date, URL, topics)
3. **`index.json`** (6+ MB) — Full index with descriptions, excerpts, and all fields

**Query flow for an AI agent:**
1. Load `topics.json` to find video IDs matching a topic
2. Load `index-compact.json` to get metadata for those IDs
3. Follow the `path` to load `summary.md` for structured context
4. Load `transcript.txt` for full verbatim content
5. Load `comments.json` to find Robert's own clarifications

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

> Last updated: 2026-03-24

| Component | Status | Count |
|-----------|--------|-------|
| YouTube metadata + comments | ✅ Complete | 2,261 videos |
| YouTube transcripts | ✅ Complete | 2,239 / 2,261 |
| AI summaries (`summary.md`) | ✅ Complete | 2,239 / 2,261 |
| Thingiverse metadata | ✅ Complete | 181 things |
| JSON indexes | ✅ Complete | — |
| CATALOG.md navigation | ✅ Complete | — |
| Per-folder README.md | ✅ Complete | — |

---

## Contributing

This is a community archive. If you notice missing videos, incorrect metadata,
or broken links, please open an issue or pull request.

---

*Built with love by fans, for fans. Robert Murray-Smith's curiosity and
generosity in sharing his knowledge inspired many — this archive aims to
ensure his freely available work remains accessible.*
