# 03: Eager Preloading & FastMCP Tools Integration

**What to build:** Integrate the optimized search engine into the FastMCP server, ensuring eager index loading during server startup so that the first tool invocation incurs zero lazy-loading delay while keeping all tool interfaces fully backward compatible.

**Blocked by:** 02: In-Memory Inverted Token Index & Fast-Path Engine

**Status:** ready-for-agent

- [x] `NativesManager` eagerly preloads and indexes data on module import or server startup
- [x] `search_natives` tool returns fast token-efficient search results using the new inverted index
- [x] `get_native_detail` tool returns full native metadata using O(1) direct dictionary lookup
- [x] Existing MCP tool schemas and responses remain 100% backward compatible
