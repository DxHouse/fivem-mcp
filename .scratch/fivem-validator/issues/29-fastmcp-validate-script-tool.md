# 29: FastMCP validate_script Tool Integration & Documentation

**What to build:** Expose `validate_script` as an MCP tool in `src/fivem_mcp/server.py`, update `README.md` and `CONTEXT.md`.

**Blocked by:** 28: Core ScriptValidator Engine & Static Analysis Rules & ADR 0008

**Status:** ready-for-agent

- [x] `@mcp.tool() def validate_script(code: str, environment: str = "auto") -> dict[str, Any]` registered in `server.py`
- [x] `README.md` and `CONTEXT.md` updated with `validate_script` tool documentation
- [x] FastMCP CLI inspection validates 6 tools, 10 prompts, 1 resource template
