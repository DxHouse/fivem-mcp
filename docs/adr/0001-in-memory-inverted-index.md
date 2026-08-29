# 0001: In-Memory Inverted Index for Native Search

We chose an in-memory inverted token index with direct hash/name fast paths over SQLite FTS5 or runtime linear scanning. The dataset consists of ~6,400 native records (~2.7MB JSON), which fits easily into memory and takes <40ms to load. In-memory indexing delivers sub-0.1ms query latencies and zero external database file management, while providing multi-word token matching and relevance scoring.
