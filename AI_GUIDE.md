# AI Guide: Robert Murray-Smith Fan Archive

This file tells you — an AI model — how to navigate and query this archive effectively.

---

## What This Archive Is

A comprehensive fan archive of **Robert Murray-Smith's** work:

- **2,261 YouTube videos** across 3 channels: `@ThinkingandTinkering`, `@TnTtalktime`, `@TnTOmnibus`
- **181 Thingiverse 3D designs**

Robert was a prolific inventor and educator based in Scotland, covering graphene synthesis, batteries, supercapacitors, solar cells, electrochemistry, 3D printing, material science, and DIY electronics — often with kitchen-table experiments. He passed away in 2024.

This is an unofficial preservation archive, not affiliated with his estate.

---

## Repository Structure

```
(repo root)/
├── index.json                         ← Master index — ALL items, all platforms
├── AI_GUIDE.md                        ← This file
├── README.md                          ← Human-facing overview
├── CATALOG.md                         ← Human-readable browsable index (all content)
├── youtube/
│   ├── index.json                     ← All YouTube videos
│   ├── CATALOG.md                     ← YouTube browsing index
│   ├── ThinkingandTinkering/
│   │   ├── index.json
│   │   ├── CATALOG.md
│   │   └── {video_id}/
│   │       ├── metadata.json
│   │       ├── transcript.txt
│   │       ├── summary.md
│   │       └── comments.json
│   ├── TnTtalktime/
│   │   └── (same structure)
│   └── TnTOmnibus/
│       └── (same structure)
├── 3d-files/
│   └── thingiverse/
│       ├── index.json
│       ├── CATALOG.md
│       └── {thing_id}/
│           ├── metadata.json
│           └── files/                 ← .stl, .3mf, etc.
└── scripts/                           ← Archive build tooling
```

---

## How to Query This Archive

### Finding videos by topic

Load `index.json`. Each entry has `key_topics` (array) and `materials_mentioned` (array). Search these fields plus `title` and `description`.

```
index.json → filter entries where key_topics contains "graphene"
           → returns list of {title, url, path, summary_excerpt}
```

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

- `youtube/{channel}/index.json` — all videos for that channel
- `youtube/{channel}/CATALOG.md` — human-readable list

Channels: `ThinkingandTinkering` (main), `TnTtalktime` (talks/interviews), `TnTOmnibus` (compilations).

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
| `channel` | string | Channel handle, e.g. `"ThinkingandTinkering"` |
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

## Notes on Archive Completeness

As of 2026-03-19:
- Metadata and comments: complete for all 2,261 videos
- Transcripts: partial (37 / 2,261) due to IP blocking during collection
- AI summaries (`summary.md`): not yet generated — check `has_summary` before loading
- `key_topics` and `materials_mentioned`: populated only where `has_summary` is true
- Thingiverse files: complete (181 things)

When `has_transcript` or `has_summary` is false, fall back to `description` and `tags` from metadata.
