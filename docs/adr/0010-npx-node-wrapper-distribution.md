# 0010: NPX Node.js Wrapper Distribution

We introduced a lightweight Node.js wrapper package (`@dxhouse/fivem-mcp`) with an executable `bin/cli.js` alongside the Python codebase in root `package.json`.

Rather than rewriting the FastMCP Python server in TypeScript, the Node CLI acts as a thin launcher that delegates execution to `uvx` / `uv` (`uvx --from git+https://github.com/DxHouse/fivem-mcp fivem-mcp`).

This provides:
1. **Zero-Friction MCP Client Setup**: Developers can configure Claude Desktop, Cursor, or Windsurf using the standard `"command": "npx", "args": ["-y", "@dxhouse/fivem-mcp"]` convention without cloning the repo locally.
2. **Single Codebase**: Python remains the single source of truth for native lookups, documentation engines, and Lua static analysis.
3. **Graceful Fallback**: If `uv` is absent on the host, the CLI displays immediate one-line installation commands for PowerShell and bash before exiting.
