# 02: In-Memory Inverted Token Index & Fast-Path Engine

**What to build:** An in-memory inverted token search engine that parses function names, namespaces, and descriptions into normalized alphanumeric tokens, builds index mappings, supports multi-word AND/OR queries, provides O(1) exact hash and name fast-paths, and precomputes formatted summary records.

**Blocked by:** 01: Domain Modeling & ADR Setup

**Status:** ready-for-agent

- [x] Alphanumeric tokenizer handles snake_case, camelCase, and space delimiters
- [x] Inverted index maps normalized tokens to native record IDs
- [x] Direct O(1) lookup dictionary for exact hashes and normalized function names
- [x] Pre-formatted summary and signature cache stored in index memory to eliminate query-time string formatting
- [x] Multi-word queries evaluate candidate matches with token set intersection and relevance ranking
