# 24: Frontmatter Parser & Search Keyword Weighting in DocsManager & ADR 0007

**What to build:** Add zero-dependency YAML frontmatter extraction in `src/fivem_mcp/docs.py`, index keyword synonyms with +100 search scoring boost, and create `docs/adr/0007-documentation-optimization-and-indexing.md`.

**Blocked by:** None (can start immediately)

**Status:** ready-for-agent

- [x] `DocsManager` parses `title`, `description`, and `keywords` from frontmatter
- [x] `_keyword_tokens` indexed with high priority (+100 score) in `DocsManager.search()`
- [x] `docs/adr/0007-documentation-optimization-and-indexing.md` created
