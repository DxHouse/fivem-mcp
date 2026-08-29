# 11: Specialized MCP Prompts & Templates Integration

**What to build:** Add specialized scaffolding prompts (`scaffold_nui_resource`, `scaffold_dui_screen`, `scaffold_csharp_resource`) to `src/fivem_mcp/server.py` and verify all 17 doc topics resolve via `docs://fivem/{topic}` resources.

**Blocked by:** 10: Developer Guides Batch 2 (UI, Audio & New Game Features)

**Status:** ready-for-agent

- [x] `@mcp.prompt("scaffold_nui_resource")` implemented with Web UI frontend boilerplate
- [x] `@mcp.prompt("scaffold_dui_screen")` implemented with 3D render target mapping boilerplate
- [x] `@mcp.prompt("scaffold_csharp_resource")` implemented with `.csproj` and `BaseScript` boilerplate
- [x] FastMCP CLI inspection validates all 4 prompts and all resource templates
