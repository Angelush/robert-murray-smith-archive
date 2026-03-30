"""
mcp_server.py — MCP server for the Robert Murray-Smith fan archive.

Exposes search and retrieval tools so any MCP-compatible AI
(Claude Desktop, Claude Code, etc.) can query the archive directly.

Usage:
    python mcp_server.py [--archive-root /path/to/archive]

Claude Desktop config (claude_desktop_config.json):
    {
      "mcpServers": {
        "rob-archive": {
          "command": "python",
          "args": ["/path/to/mcp_server.py"]
        }
      }
    }
"""

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

# Import the shared search library (same directory)
from archive_search import ArchiveSearch

# ---------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------

app = Server("rob-archive")
archive: ArchiveSearch | None = None

# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------

@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="search_topics",
            description=(
                "Search Robert Murray-Smith's video archive by topic or material keyword. "
                "Fast lookup — returns matching videos sorted by date. "
                "Good for: 'graphene', 'supercapacitor', 'battery', 'solar cell', etc."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Topic or material to search for",
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Max results to return (default 10)",
                        "default": 10,
                    },
                },
                "required": ["query"],
            },
        ),
        Tool(
            name="search_videos",
            description=(
                "Semantic search across all 2,261 videos using natural language. "
                "Best for questions like 'how to make a supercapacitor from coconut shells'. "
                "Uses AI embeddings if available, otherwise falls back to keyword search."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Natural language search query",
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Max results to return (default 5)",
                        "default": 5,
                    },
                },
                "required": ["query"],
            },
        ),
        Tool(
            name="get_video",
            description=(
                "Get full details for a specific video: metadata, AI summary, and optionally "
                "the full transcript. Use video_id from search results."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "video_id": {
                        "type": "string",
                        "description": "YouTube video ID (e.g., 'dQw4w9WgXcQ')",
                    },
                    "include_transcript": {
                        "type": "boolean",
                        "description": "Include full transcript text (can be large). Default false.",
                        "default": False,
                    },
                },
                "required": ["video_id"],
            },
        ),
        Tool(
            name="get_3d_design",
            description=(
                "Get details for a Thingiverse 3D design: name, description, STL file list, "
                "and related videos. Use thing_id from search results or video cross-references."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "thing_id": {
                        "type": "string",
                        "description": "Thingiverse thing ID (e.g., '7150252')",
                    },
                },
                "required": ["thing_id"],
            },
        ),
        Tool(
            name="list_channels",
            description=(
                "List Robert Murray-Smith's YouTube channels with video counts. "
                "3 channels: ThinkingandTinkering (main), TnTtalktime (talks), TnTOmnibus (compilations)."
            ),
            inputSchema={
                "type": "object",
                "properties": {},
            },
        ),
        Tool(
            name="get_random_video",
            description="Get a random video recommendation from the archive.",
            inputSchema={
                "type": "object",
                "properties": {},
            },
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if archive is None:
        return [TextContent(type="text", text="Error: archive not initialized")]

    try:
        if name == "search_topics":
            results = archive.search_topics(
                arguments["query"],
                limit=arguments.get("limit", 10),
            )
            return [TextContent(
                type="text",
                text=json.dumps([asdict(r) for r in results], indent=2, ensure_ascii=False),
            )]

        elif name == "search_videos":
            results = archive.search_videos(
                arguments["query"],
                limit=arguments.get("limit", 5),
            )
            return [TextContent(
                type="text",
                text=json.dumps([asdict(r) for r in results], indent=2, ensure_ascii=False),
            )]

        elif name == "get_video":
            video = archive.get_video(
                arguments["video_id"],
                include_transcript=arguments.get("include_transcript", False),
            )
            if video is None:
                return [TextContent(type="text", text=f"Video '{arguments['video_id']}' not found")]
            return [TextContent(
                type="text",
                text=json.dumps(asdict(video), indent=2, ensure_ascii=False),
            )]

        elif name == "get_3d_design":
            design = archive.get_3d_design(arguments["thing_id"])
            if design is None:
                return [TextContent(type="text", text=f"Design '{arguments['thing_id']}' not found")]
            return [TextContent(
                type="text",
                text=json.dumps(asdict(design), indent=2, ensure_ascii=False),
            )]

        elif name == "list_channels":
            channels = archive.list_channels()
            data = {
                "channels": [asdict(c) for c in channels],
                "stats": asdict(archive.stats),
            }
            return [TextContent(
                type="text",
                text=json.dumps(data, indent=2, ensure_ascii=False),
            )]

        elif name == "get_random_video":
            video = archive.get_random_video()
            if video is None:
                return [TextContent(type="text", text="No videos found in archive")]
            return [TextContent(
                type="text",
                text=json.dumps(asdict(video), indent=2, ensure_ascii=False),
            )]

        else:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {e}")]


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

async def main():
    global archive

    parser = argparse.ArgumentParser(description="MCP server for Rob archive")
    parser.add_argument(
        "--archive-root",
        type=str,
        default=str(Path(__file__).parent),
        help="Path to archive root (default: directory containing this script)",
    )
    parser.add_argument(
        "--chroma-dir",
        type=str,
        default=None,
        help="Path to ChromaDB directory (default: archive_root/chroma_db)",
    )
    args = parser.parse_args()

    archive = ArchiveSearch(args.archive_root, args.chroma_dir)
    stats = archive.stats
    print(
        f"Rob Archive MCP Server ready: {stats.total_videos} videos, "
        f"{stats.total_3d_items} 3D designs, "
        f"ChromaDB: {'yes' if stats.has_chromadb else 'no (keyword-only)'}",
        file=sys.stderr,
    )

    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
