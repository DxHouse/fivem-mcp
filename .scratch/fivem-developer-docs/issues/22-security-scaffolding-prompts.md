# 22: FastMCP Server Security Scaffolding Prompts Integration

**What to build:** Add security scaffolding prompts (`scaffold_secure_event_handler`, `scaffold_safe_transaction`) to `src/fivem_mcp/server.py` and verify all 33 doc topics resolve via `docs://fivem/{topic}` resources.

**Blocked by:** 21: Developer Docs (Sandbox, Script Runtimes & Server Security) & ADR 0006

**Status:** ready-for-agent

- [x] `@mcp.prompt("scaffold_secure_event_handler")` implemented with `source` capturing, rate limiting, and distance validation
- [x] `@mcp.prompt("scaffold_safe_transaction")` implemented with authoritative state locking and race condition mutexes
- [x] FastMCP CLI inspection validates all 10 prompts and all resource templates
