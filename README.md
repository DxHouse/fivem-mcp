# fivem-mcp

FastMCP Server Framework for FiveM built with `uv`.

## Requirements

- Python >= 3.11
- [uv](https://docs.astral.sh/uv/)

## Getting Started

1. **Install dependencies:**
   ```bash
   uv sync
   ```

2. **Run server (STDIO):**
   ```bash
   uv run fivem-mcp
   ```

3. **FastMCP Inspector (Web UI):**
   ```bash
   uv run fastmcp dev inspector src/fivem_mcp/server.py
   ```

4. **Inspect Tools Summary (CLI):**
   ```bash
   uv run fastmcp inspect src/fivem_mcp/server.py
   ```

## Client Configuration (Claude Desktop / Cursor)

Add to your MCP configuration file (e.g. `claude_desktop_config.json` or `.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "fivem-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "E:\\WorkStation\\VibeCoding\\fivem-mcp",
        "run",
        "fivem-mcp"
      ]
    }
  }
}
```
