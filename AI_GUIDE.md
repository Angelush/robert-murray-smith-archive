# AI Guide: Robert Murray-Smith Fan Archive

This file tells you — an AI model — how to navigate and query this archive effectively.

---

## What This Archive Is

A comprehensive fan archive of **Robert Murray-Smith's** publicly available, free YouTube content:

- **2,261 YouTube videos** across 3 channels: `@ThinkingandTinkering`, `@TnTtalktime`, `@TnTOmnibus`
- **181 Thingiverse 3D designs**

**Important:** This archive only contains free, publicly available content. It does not include any channel-members-only videos or paid content.

Robert was a prolific inventor and educator covering graphene synthesis, batteries, supercapacitors, solar cells, electrochemistry, 3D printing, material science, and DIY electronics — often with kitchen-table experiments. He passed away in 2025.

This is an unofficial preservation archive, not affiliated with his estate.

---

## MCP Server

This archive includes an MCP server. If you're connected via MCP, use the provided tools directly:
- `search_topics("graphene")` — fast keyword lookup
- `search_videos("how to make a supercapacitor")` — semantic search
- `get_video("VIDEO_ID")` — full video details + summary
- `get_3d_design("THING_ID")` — 3D design metadata

You don't need to read index files manually — the tools handle everything.

---

## Repository Structure

```
(repo root)/
├── index.json                         ← Master index — ALL items, all platforms (6+ MB)
├── index-compact.json                 ← Compact index for AI queries (~500 KB)
├── topics.json                        ← Inverted topic/material index (~100 KB)
├── AI_GUIDE.md                        ← This file
├── README.md                          ← Human-facing overview
├── CATALOG.md                         ← Human-readable browsable index (all content)
├── build_vectordb.py                  ← Build ChromaDB for semantic search
├── mcp_server.py                      ← MCP server for AI tool access
├── youtube/
│   ├── index.json                     ← All YouTube videos
│   ├── CATALOG.md                     ← YouTube browsing index
│   ├── @ThinkingandTinkering/
│   │   ├── index.json
│   │   ├── CATALOG.md
│   │   └── {video_id}/
│   │       ├── metadata.json
│   │       ├── transcript.txt
│   │       ├── summary.md
│   │       ├── comments.json
│   │       └── README.md
│   ├── @TnTtalktime/
│   │   └── (same structure)
│   └── @TnTOmnibus/
│       └── (same structure)
├── 3d-files/
│   └── thingiverse/
│       ├── index.json
│       ├── CATALOG.md
│       └── {thing_id}/
│           ├── README.md              ← Auto-rendered: name, link, description
│           └── metadata.json
```

---

## How to Query This Archive

### Finding videos by topic

For most queries, use `topics.json` first — it maps topic and material names directly to video IDs, costing far fewer tokens than loading `index.json`.

```
topics.json → look up "graphene" → get list of video IDs
index-compact.json → load metadata for those IDs
{path}/summary.md → load full context for each
```

If you need to do a broad scan of all items, use `index-compact.json` rather than `index.json` — it is ~10x smaller and contains all the fields needed for topic filtering.

For browsing without code, open `CATALOG.md` or `youtube/CATALOG.md` — these are human-readable tables of all content.

### Reading a video's full content

Given a match from `index.json`, the `path` field gives the directory:

- `{path}/transcript.txt` — full verbatim transcript with timestamps
- `{path}/summary.md` — structured AI summary (topics, materials, techniques, timestamps, Robert's own comment replies)
- `{path}/metadata.json` — title, date, view count, tags, URL
- `{path}/comments.json` — all comments and replies

Start with `summary.md` for speed. Use `transcript.txt` for precise quotes or full context.

### Finding 3D files related to a video

Two ways:
1. Check `related_3d_files` in a video's index entry — it lists linked Thingiverse thing IDs.
2. Check `related_videos` in `3d-files/thingiverse/{thing_id}/metadata.json` — links back to videos.

### Browsing by channel

- `youtube/@{channel}/index.json` — all videos for that channel
- `youtube/@{channel}/CATALOG.md` — human-readable list

Channels: `@ThinkingandTinkering` (main), `@TnTtalktime` (talks/interviews), `@TnTOmnibus` (compilations).

### Full-text search across transcripts

Transcripts are plain `.txt` files. If you can run grep or glob:

```
youtube/**/{video_id}/transcript.txt
```

Search for any term across all transcripts.

---

## Index Entry Fields (YouTube Video)

| Field | Type | Contents |
|-------|------|----------|
| `type` | string | Always `"video"` |
| `platform` | string | Always `"youtube"` |
| `channel` | string | Channel handle, e.g. `"@ThinkingandTinkering"` |
| `video_id` | string | YouTube video ID, e.g. `"dQw4w9WgXcQ"` |
| `title` | string | Video title |
| `description` | string | YouTube description (may be truncated) |
| `published_at` | string | ISO 8601 date, e.g. `"2021-03-15T10:00:00Z"` |
| `duration` | string | ISO 8601 duration, e.g. `"PT18M42S"` |
| `tags` | array | YouTube tags as set by Robert |
| `view_count` | integer | View count at time of archiving |
| `like_count` | integer | Like count at time of archiving |
| `url` | string | Full YouTube URL |
| `thumbnail` | string | Thumbnail URL |
| `has_transcript` | boolean | Whether `transcript.txt` exists |
| `has_summary` | boolean | Whether `summary.md` exists |
| `comment_count_archived` | integer | Number of comments archived |
| `summary_excerpt` | string | First 2–3 sentences of the AI summary |
| `key_topics` | array | AI-extracted topic tags, e.g. `["graphene", "supercapacitors"]` |
| `materials_mentioned` | array | Materials/chemicals named in video, e.g. `["graphene oxide", "KOH"]` |
| `path` | string | Relative path to video directory from repo root |
| `related_3d_files` | array | Thing IDs of related Thingiverse designs (may be empty) |

---

## Example Queries and How to Answer Them

**"Find all graphene videos"**
Load `index.json`. Filter entries where `key_topics` or `materials_mentioned` contains `"graphene"`. Return titles, URLs, and `summary_excerpt` for each match.

**"What battery chemistries does Robert explore?"**
Filter `index.json` where `key_topics` contains `"batteries"` or `"battery"`. Collect all unique values from `materials_mentioned` across those entries. Read `summary.md` for the most-viewed ones to get detail.

**"Show me videos with 3D printable files"**
Filter `index.json` entries where `related_3d_files` is non-empty. Also browse `3d-files/thingiverse/index.json` and follow `related_videos` links.

**"Summarize Robert's work on supercapacitors"**
1. Filter `index.json` for `key_topics` containing `"supercapacitors"`.
2. For each match, load `{path}/summary.md`.
3. Synthesize across summaries: common materials, methods, conclusions, evolution over time.

**"What does Robert say about using activated charcoal in supercapacitors?"**
Find supercapacitor videos as above. Search `transcript.txt` files for "activated charcoal". Pull relevant passages.

**"List all 3D designs Robert made for battery holders"**
Load `3d-files/thingiverse/index.json`. Filter by `tags` or `name` containing relevant terms. Check `related_videos` to find the video where he explains the design.

---

## Token-Efficient Indexes

For large queries, `index.json` (6+ MB) may consume too many tokens. Use these smaller alternatives:

### `index-compact.json` (~500 KB)
Stripped-down index with short field names. Contains all 2,442 items with: id, type (`yt`/`tv`), title (`t`), date (`d`), channel abbreviation (`ch`), topics, materials, url, path, and cross-references.

**Use this** as your default starting point instead of `index.json`.

### `topics.json` (~100 KB)
Inverted index: topic → list of video IDs, and material → list of video IDs.

**Use this** when answering "find all videos about X" — load just this file, find matching video IDs, then load only those items from `index-compact.json` or directly load their `summary.md` files.

### Recommended query flow
1. Load `topics.json` → find video IDs matching the query topic
2. Load `index-compact.json` → get metadata for those IDs
3. Load `{path}/summary.md` for each → get full structured summaries
4. Load `{path}/transcript.txt` only if you need verbatim quotes

---

## Notes on Archive Completeness

As of 2026-03-24:
- Metadata and comments: complete for all 2,261 videos
- Transcripts: 2,239 / 2,261 (22 videos have no transcript available)
- AI summaries (`summary.md`): 2,239 / 2,261 generated
- `key_topics` and `materials_mentioned`: populated for all videos with summaries (2,239)
- Thingiverse files: complete (181 things)

When `has_transcript` or `has_summary` is false, fall back to `description` and `tags` from metadata.
