# 01: Domain Modeling & ADR Setup

**What to build:** Establish the canonical domain glossary and architectural decision records for the FiveM MCP server, creating a ubiquitous language for native function entities, namespaces, hashes, execution environments, and documenting the in-memory inverted index architecture.

**Blocked by:** None (can start immediately)

**Status:** ready-for-agent

- [x] `CONTEXT.md` exists at root defining `Native`, `Namespace`, `Hash`, `APISet`, `Client`, `Server`, and `Signature`
- [x] `docs/adr/0001-in-memory-inverted-index.md` records the trade-offs and decision to use in-memory token indexing over SQLite FTS5 and linear scan
