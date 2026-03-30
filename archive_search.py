"""
archive_search.py — Shared search library for the Rob archive MCP server and Discord bot.

Data layout:
  index-compact.json  — top-level: {items: [{id, type, t, d, ch, topics, materials, url, path, 3d|vids}]}
                         type = "yt" (YouTube), "tv" (Thingiverse), "Talk", etc.
                         ch   = "TT" | "Omni" | "Talk" | "" (Thingiverse has no ch)
  topics.json         — {topics: {topic_str: [video_id, ...]}, materials: {mat_str: [video_id, ...]}}
  3d-files/index.json — {items: [{type, platform, thing_id, name, description, tags, license, url, thumbnail, files, related_videos, path, ...}]}
  youtube/<channel>/<video_id>/metadata.json  — full video metadata
  youtube/<channel>/<video_id>/summary.md     — AI-generated summary
  youtube/<channel>/<video_id>/transcript.txt — full transcript (optional)
"""

from dataclasses import dataclass, asdict
from pathlib import Path
import json
import re
import random
import logging

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

log = logging.getLogger("archive_search")

# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class VideoResult:
    video_id: str
    title: str
    url: str
    date: str
    channel: str
    summary_text: str   # chunk text from ChromaDB or summary overview paragraph
    relevance: float    # 0.0 = perfect cosine match, higher = less similar


@dataclass
class CompactEntry:
    id: str
    type: str           # "yt", "tv", "Omni", "Talk", …
    title: str
    date: str
    channel: str        # full handle e.g. "@ThinkingandTinkering", or "" for 3d
    topics: list
    materials: list
    url: str
    path: str
    three_d: list       # list of related thing_ids (for yt items) or related video_ids (for tv items)


@dataclass
class VideoDetail:
    video_id: str
    title: str
    description: str
    published_at: str
    channel: str
    tags: list
    duration: str
    view_count: int
    like_count: int
    url: str
    thumbnail: str
    summary: str | None
    transcript: str | None
    topics: list
    materials: list
    path: str


@dataclass
class ThingiverseEntry:
    thing_id: str
    name: str
    description: str
    tags: list
    license: str
    url: str
    thumbnail: str
    files: list
    related_videos: list
    path: str


@dataclass
class ChannelInfo:
    handle: str
    abbreviation: str
    video_count: int


@dataclass
class ArchiveStats:
    total_videos: int
    total_3d_items: int
    total_topics: int
    total_materials: int
    channels: list
    has_chromadb: bool


# ---------------------------------------------------------------------------
# ArchiveSearch
# ---------------------------------------------------------------------------

class ArchiveSearch:
    # Maps compact index abbreviations → full YouTube handles
    CHANNEL_MAP = {
        "TT":   "@ThinkingandTinkering",
        "Omni": "@TnTOmnibus",
        "Talk": "@TnTtalktime",
    }

    def __init__(self, archive_root: str | Path, chroma_dir: str | Path | None = None):
        self._root = Path(archive_root)
        self._compact_index: dict[str, dict] = {}   # id -> raw compact item
        self._topics_index: dict[str, list[str]] = {}
        self._materials_index: dict[str, list[str]] = {}
        self._3d_index: dict[str, dict] = {}         # thing_id -> raw 3d item
        self._chromadb_available = False
        self._collection = None
        # TF-IDF search (lightweight fallback when ChromaDB unavailable)
        self._tfidf_vectorizer: TfidfVectorizer | None = None
        self._tfidf_matrix = None
        self._tfidf_ids: list[str] = []       # video_id at each row index
        self._summary_cache: dict[str, str] = {}  # video_id -> full summary text

        self._load_indexes()
        self._init_chromadb(chroma_dir)
        if not self._chromadb_available:
            self._init_tfidf()

    # ------------------------------------------------------------------
    # Index loading
    # ------------------------------------------------------------------

    def _load_indexes(self):
        compact_path = self._root / "index-compact.json"
        topics_path  = self._root / "topics.json"
        td_path      = self._root / "3d-files" / "index.json"

        if compact_path.exists():
            with open(compact_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            items = data if isinstance(data, list) else data.get("items", [])
            for item in items:
                vid = item.get("id", "")
                if vid:
                    self._compact_index[vid] = item
            log.info("Loaded %d items from index-compact.json", len(self._compact_index))
        else:
            log.warning("index-compact.json not found at %s", compact_path)

        if topics_path.exists():
            with open(topics_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self._topics_index.update(data.get("topics", {}))
            self._materials_index.update(data.get("materials", {}))
            log.info(
                "Loaded %d topics, %d materials",
                len(self._topics_index),
                len(self._materials_index),
            )
        else:
            log.warning("topics.json not found at %s", topics_path)

        if td_path.exists():
            with open(td_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            items = data if isinstance(data, list) else data.get("items", [])
            for item in items:
                tid = item.get("thing_id", "")
                if tid:
                    self._3d_index[tid] = item
            log.info("Loaded %d 3d designs from 3d-files/index.json", len(self._3d_index))
        else:
            log.warning("3d-files/index.json not found at %s", td_path)

    # ------------------------------------------------------------------
    # ChromaDB initialisation (optional)
    # ------------------------------------------------------------------

    def _init_chromadb(self, chroma_dir: str | Path | None):
        try:
            import chromadb
            from chromadb.utils import embedding_functions

            if chroma_dir is None:
                # Look for a chroma/ or chromadb/ directory next to the archive root
                for candidate in ("chroma", "chromadb", ".chroma"):
                    p = self._root / candidate
                    if p.exists():
                        chroma_dir = p
                        break

            if chroma_dir is None or not Path(chroma_dir).exists():
                log.info("chroma_dir not found — ChromaDB disabled")
                return

            ef = embedding_functions.SentenceTransformerEmbeddingFunction(
                model_name="all-MiniLM-L6-v2"
            )
            client = chromadb.PersistentClient(path=str(chroma_dir))
            self._collection = client.get_or_create_collection(
                name="rob_videos",
                embedding_function=ef,
                metadata={"hnsw:space": "cosine"},
            )

            if self._collection.count() == 0:
                log.info("ChromaDB collection 'rob_videos' is empty — semantic search disabled")
                self._collection = None
                return

            self._chromadb_available = True
            log.info(
                "ChromaDB ready — %d vectors in 'rob_videos'",
                self._collection.count(),
            )

        except ImportError:
            log.info("chromadb not installed — falling back to keyword search")
        except (Exception, RecursionError, SystemError) as exc:
            log.warning("ChromaDB init failed (%s) — falling back to keyword search", exc)
        except BaseException as exc:
            log.warning("ChromaDB init failed with %s: %s — falling back to keyword search", type(exc).__name__, exc)

    # ------------------------------------------------------------------
    # TF-IDF initialisation (lightweight fallback for semantic-ish search)
    # ------------------------------------------------------------------

    def _init_tfidf(self):
        """Build a TF-IDF index from all video summaries, titles, topics, and descriptions."""
        documents: list[str] = []
        ids: list[str] = []

        for vid_id, raw in self._compact_index.items():
            if raw.get("type") not in ("yt", "TT", "Omni", "Talk", None):
                continue  # skip Thingiverse for TF-IDF

            parts = []
            # Title (weighted by repetition for importance)
            title = raw.get("t", "")
            parts.append(title)
            parts.append(title)

            # Description from compact index
            desc = raw.get("d", "")
            if desc:
                parts.append(desc)

            # Topics and materials
            parts.extend(raw.get("topics", []))
            parts.extend(raw.get("materials", []))

            # Read full summary from disk
            vid_path = raw.get("path", "")
            summary_path = self._root / vid_path / "summary.md"
            summary_text = ""
            if summary_path.exists():
                try:
                    summary_text = summary_path.read_text(encoding="utf-8")
                    parts.append(summary_text)
                except Exception:
                    pass

            doc_text = "\n".join(parts)
            if doc_text.strip():
                documents.append(doc_text)
                ids.append(vid_id)
                self._summary_cache[vid_id] = summary_text

        if not documents:
            log.warning("No documents found for TF-IDF index")
            return

        self._tfidf_vectorizer = TfidfVectorizer(
            max_features=50000,
            stop_words="english",
            ngram_range=(1, 2),
            sublinear_tf=True,
        )
        self._tfidf_matrix = self._tfidf_vectorizer.fit_transform(documents)
        self._tfidf_ids = ids
        log.info("TF-IDF index ready — %d documents, %d features",
                 len(ids), self._tfidf_matrix.shape[1])

    def _tfidf_search(self, query: str, limit: int) -> list[VideoResult]:
        """Search using TF-IDF cosine similarity."""
        query_vec = self._tfidf_vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self._tfidf_matrix).flatten()
        top_indices = np.argsort(scores)[::-1][:limit]

        results = []
        for idx in top_indices:
            score = scores[idx]
            if score < 0.01:
                break
            vid_id = self._tfidf_ids[idx]
            raw = self._compact_index.get(vid_id)
            if not raw:
                continue
            entry = self._raw_to_compact_entry(raw)
            # Use cached summary for richer LLM context
            summary_text = self._summary_cache.get(vid_id, "")
            if not summary_text:
                summary_text = entry.title
            results.append(VideoResult(
                video_id=entry.id,
                title=entry.title,
                url=entry.url,
                date=entry.date,
                channel=entry.channel,
                summary_text=summary_text,
                relevance=1.0 - score,  # convert similarity to distance-like
            ))
        return results

    # ------------------------------------------------------------------
    # Public: search_videos
    # ------------------------------------------------------------------

    def search_videos(
        self,
        query: str,
        limit: int = 8,
        min_relevance: float = 0.3,
    ) -> list[VideoResult]:
        """
        Search priority: ChromaDB (semantic) → TF-IDF (summary-aware) → keyword.

        relevance is the cosine distance: 0.0 = perfect match, 1.0 = unrelated.
        min_relevance is the MAXIMUM allowed distance (lower = stricter filter).
        """
        if self._chromadb_available and self._collection is not None:
            return self._chromadb_search(query, limit, min_relevance)
        if self._tfidf_vectorizer is not None:
            return self._tfidf_search(query, limit)
        # Final fallback: keyword only
        compact_results = self.search_topics(query, limit=limit)
        return [self._compact_to_video_result(e) for e in compact_results]

    def _chromadb_search(
        self,
        query: str,
        limit: int,
        min_relevance: float,
    ) -> list[VideoResult]:
        # Request more results than needed to allow deduplication
        n_results = min(limit * 4, self._collection.count())
        results = self._collection.query(
            query_texts=[query],
            n_results=n_results,
            include=["documents", "metadatas", "distances"],
        )

        if not results["ids"][0]:
            return []

        # Deduplicate by video_id, keep lowest (best) distance per video
        # min_relevance is the max allowed distance (cosine: 0.0 best, 1.0 worst)
        distance_threshold = min_relevance  # e.g. 0.3 means only keep dist <= 0.3
        seen: dict[str, dict] = {}

        for i, doc_id in enumerate(results["ids"][0]):
            meta = results["metadatas"][0][i]
            distance = results["distances"][0][i]
            vid = meta.get("video_id", doc_id)

            if distance > distance_threshold:
                continue

            if vid not in seen or distance < seen[vid]["distance"]:
                seen[vid] = {
                    "video_id": vid,
                    "title": meta.get("title", "Untitled"),
                    "url": meta.get("url", f"https://www.youtube.com/watch?v={vid}"),
                    "date": meta.get("date", ""),
                    "channel": meta.get("channel", ""),
                    "document": results["documents"][0][i],
                    "distance": distance,
                }

        ranked = sorted(seen.values(), key=lambda x: x["distance"])[:limit]

        return [
            VideoResult(
                video_id=r["video_id"],
                title=r["title"],
                url=r["url"],
                date=r["date"],
                channel=r["channel"],
                summary_text=r["document"],
                relevance=r["distance"],
            )
            for r in ranked
        ]

    def _compact_to_video_result(self, entry: CompactEntry) -> VideoResult:
        # Read summary overview paragraph if available
        summary_text = ""
        summary_path = self._root / entry.path / "summary.md"
        if summary_path.exists():
            try:
                text = summary_path.read_text(encoding="utf-8")
                # Extract the first paragraph under ## Overview
                m = re.search(r"##\s*Overview\s*\n+(.+?)(?:\n\n|\n##)", text, re.DOTALL)
                summary_text = m.group(1).strip() if m else text[:500]
            except Exception:
                pass

        return VideoResult(
            video_id=entry.id,
            title=entry.title,
            url=entry.url,
            date=entry.date,
            channel=entry.channel,
            summary_text=summary_text,
            relevance=0.5,  # unknown distance for keyword results
        )

    # ------------------------------------------------------------------
    # Public: search_topics
    # ------------------------------------------------------------------

    def search_topics(self, query: str, limit: int = 10) -> list[CompactEntry]:
        """
        Keyword search against topics, materials, and video titles.
        Returns CompactEntry objects sorted by date descending.
        """
        query_lower = query.lower().strip()
        query_words = query_lower.split()
        matching_ids: set[str] = set()

        # Search topics index
        for topic, vid_ids in self._topics_index.items():
            if query_lower in topic.lower():
                matching_ids.update(vid_ids)

        # Search materials index
        for material, vid_ids in self._materials_index.items():
            if query_lower in material.lower():
                matching_ids.update(vid_ids)

        # Search video titles and descriptions (catches queries topics miss)
        if len(matching_ids) < limit:
            for vid_id, raw in self._compact_index.items():
                if vid_id in matching_ids:
                    continue
                title = raw.get("t", "").lower()
                desc = raw.get("d", "").lower()
                text = title + " " + desc
                if all(w in text for w in query_words):
                    matching_ids.add(vid_id)

        results = []
        for vid_id in matching_ids:
            raw = self._compact_index.get(vid_id)
            if raw:
                results.append(self._raw_to_compact_entry(raw))

        results.sort(key=lambda e: e.date, reverse=True)
        return results[:limit]

    # ------------------------------------------------------------------
    # Public: get_video
    # ------------------------------------------------------------------

    def get_video(
        self,
        video_id: str,
        include_transcript: bool = False,
    ) -> VideoDetail | None:
        """
        Return full VideoDetail for a video_id.
        Reads metadata.json and optionally summary.md / transcript.txt.
        """
        raw = self._compact_index.get(video_id)
        if raw is None:
            return None

        path = self._root / raw.get("path", "")
        meta_path = path / "metadata.json"

        if not meta_path.exists():
            # Return a minimal detail from compact index
            return VideoDetail(
                video_id=video_id,
                title=raw.get("t", ""),
                description="",
                published_at=raw.get("d", ""),
                channel=self.CHANNEL_MAP.get(raw.get("ch", ""), raw.get("ch", "")),
                tags=[],
                duration="",
                view_count=0,
                like_count=0,
                url=raw.get("url", ""),
                thumbnail="",
                summary=None,
                transcript=None,
                topics=raw.get("topics", []),
                materials=raw.get("materials", []),
                path=raw.get("path", ""),
            )

        with open(meta_path, "r", encoding="utf-8") as f:
            meta = json.load(f)

        # Read summary
        summary: str | None = None
        summary_path = path / "summary.md"
        if summary_path.exists():
            try:
                summary = summary_path.read_text(encoding="utf-8")
            except Exception:
                pass

        # Read transcript (optional)
        transcript: str | None = None
        if include_transcript:
            transcript_path = path / "transcript.txt"
            if transcript_path.exists():
                try:
                    transcript = transcript_path.read_text(encoding="utf-8")
                except Exception:
                    pass

        return VideoDetail(
            video_id=video_id,
            title=meta.get("title", raw.get("t", "")),
            description=meta.get("description", ""),
            published_at=meta.get("published_at", raw.get("d", "")),
            channel=self.CHANNEL_MAP.get(raw.get("ch", ""), raw.get("ch", "")),
            tags=meta.get("tags", []),
            duration=meta.get("duration", ""),
            view_count=int(meta.get("view_count", 0) or 0),
            like_count=int(meta.get("like_count", 0) or 0),
            url=meta.get("url", raw.get("url", "")),
            thumbnail=meta.get("thumbnail", ""),
            summary=summary,
            transcript=transcript,
            topics=raw.get("topics", []),
            materials=raw.get("materials", []),
            path=raw.get("path", ""),
        )

    # ------------------------------------------------------------------
    # Public: 3D designs
    # ------------------------------------------------------------------

    def get_3d_design(self, thing_id: str) -> ThingiverseEntry | None:
        raw = self._3d_index.get(str(thing_id))
        if raw is None:
            return None
        return self._raw_to_thingiverse(raw)

    def search_3d(self, query: str, limit: int = 5) -> list[ThingiverseEntry]:
        """Keyword search across 3D design names, descriptions, and tags."""
        query_lower = query.lower().strip()
        results = []
        for raw in self._3d_index.values():
            name = raw.get("name", "").lower()
            desc = raw.get("description", "").lower()
            tags = " ".join(raw.get("tags", [])).lower()
            if query_lower in name or query_lower in desc or query_lower in tags:
                results.append(self._raw_to_thingiverse(raw))
        # Sort by date added (most recent first)
        results.sort(key=lambda e: e.thing_id, reverse=True)
        return results[:limit]

    # ------------------------------------------------------------------
    # Public: channels / random / stats
    # ------------------------------------------------------------------

    def list_channels(self) -> list[ChannelInfo]:
        counts: dict[str, int] = {}
        for raw in self._compact_index.values():
            ch = raw.get("ch", "")
            if ch:
                counts[ch] = counts.get(ch, 0) + 1

        channels = []
        for abbr, handle in self.CHANNEL_MAP.items():
            channels.append(
                ChannelInfo(
                    handle=handle,
                    abbreviation=abbr,
                    video_count=counts.get(abbr, 0),
                )
            )
        return channels

    def get_random_video(self) -> CompactEntry | None:
        yt_items = [
            raw for raw in self._compact_index.values()
            if raw.get("type") == "yt"
        ]
        if not yt_items:
            return None
        return self._raw_to_compact_entry(random.choice(yt_items))

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def has_chromadb(self) -> bool:
        return self._chromadb_available

    @property
    def stats(self) -> ArchiveStats:
        total_videos = sum(
            1 for raw in self._compact_index.values()
            if raw.get("type") == "yt"
        )
        return ArchiveStats(
            total_videos=total_videos,
            total_3d_items=len(self._3d_index),
            total_topics=len(self._topics_index),
            total_materials=len(self._materials_index),
            channels=[asdict(c) for c in self.list_channels()],
            has_chromadb=self._chromadb_available,
        )

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _raw_to_compact_entry(self, raw: dict) -> CompactEntry:
        ch_abbr = raw.get("ch", "")
        full_handle = self.CHANNEL_MAP.get(ch_abbr, ch_abbr)
        item_type = raw.get("type", "yt")

        # For tv (Thingiverse) items, related vids are in "vids"; for yt, 3d links in "3d"
        three_d = raw.get("3d", raw.get("vids", []))

        return CompactEntry(
            id=raw.get("id", ""),
            type=item_type,
            title=raw.get("t", ""),
            date=raw.get("d", ""),
            channel=full_handle,
            topics=raw.get("topics", []),
            materials=raw.get("materials", []),
            url=raw.get("url", ""),
            path=raw.get("path", ""),
            three_d=three_d,
        )

    def _raw_to_thingiverse(self, raw: dict) -> ThingiverseEntry:
        return ThingiverseEntry(
            thing_id=raw.get("thing_id", ""),
            name=raw.get("name", ""),
            description=raw.get("description", ""),
            tags=raw.get("tags", []),
            license=raw.get("license", ""),
            url=raw.get("url", ""),
            thumbnail=raw.get("thumbnail", ""),
            files=raw.get("files", []),
            related_videos=raw.get("related_videos", []),
            path=raw.get("path", ""),
        )
