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

## Available MCP Capabilities

### 🛠️ Tools
- **`search_natives(query, namespace, apiset, limit)`**: Search FiveM / GTA V natives by name, hash, or description. Supports filtering by namespace (e.g. `PLAYER`, `VEHICLE`) and apiset (`all`, `client`, `server`).
- **`get_native_detail(name_or_hash)`**: Get full parameter types, return values, descriptions, and examples for a native.
- **`search_docs(query, limit)`**: Search curated FiveM developer guides (e.g. `fxmanifest`, `events`, `statebags`, `nui`).
- **`get_doc(topic)`**: Retrieve complete Markdown developer guide for a topic.
- **`ping(message)`**: Health check test tool.

### 📖 Resources
- **`docs://fivem/{topic}`**: Direct access to Markdown developer documentation (e.g. `docs://fivem/fxmanifest`, `docs://fivem/state-bags`).

### 💡 Prompts
- **`scaffold_resource(name, description, has_client, has_server, has_ui)`**: Generates complete boilerplate instructions and modern `fxmanifest.lua` configuration for a new FiveM resource.

## Data Storage

FiveM native function definitions are stored in:
```
data/natives.json
```
- If the file does not exist, the server will automatically download it from `https://runtime.fivem.net/doc/natives.json` on first run.
- You can override the path via the `FIVEM_NATIVES_PATH` environment variable.

## Development & Testing

```bash
# Run server (STDIO)
uv run fivem-mcp

# FastMCP Inspector (Web UI)
uv run fastmcp dev inspector src/fivem_mcp/server.py

# Inspect Tools Summary (CLI)
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
