# 15: FastMCP Scaffolding Prompts Integration (Deferrals & OneSync Spawner)

**What to build:** Add specialized scaffolding prompts (`scaffold_player_connecting`, `scaffold_onesync_spawner`) to `src/fivem_mcp/server.py` and verify all 21 doc topics resolve via `docs://fivem/{topic}` resources.

**Blocked by:** 14: Scripting Reference Batch 2 (Events Catalog, ConVars & OneSync)

**Status:** ready-for-agent

- [x] `@mcp.prompt("scaffold_player_connecting")` implemented with connection deferrals and identifier checks
- [x] `@mcp.prompt("scaffold_onesync_spawner")` implemented with server-setter entity creation and routing bucket support
- [x] FastMCP CLI inspection validates all 6 prompts and all resource templates
