# 06: In-Memory Docs Search Engine (DocsManager)

**What to build:** An in-memory documentation manager (`DocsManager`) in `src/fivem_mcp/docs.py` that scans all Markdown files in `data/docs/`, extracts metadata (title, summary, tags), indexes tokens into an inverted index, and provides fast search and direct topic retrieval.

**Blocked by:** 05: Core Developer Guides & Markdown Docs Content

**Status:** ready-for-agent

- [x] `DocsManager` parses and caches all Markdown files from `data/docs/`
- [x] Inverted index indexes title and content tokens for fast multi-word search
- [x] `search(query, limit)` returns matching topics with title, slug, and snippet
- [x] `get_doc(topic)` returns complete Markdown content by exact or fuzzy topic slug
