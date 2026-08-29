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
- **`validate_script(code, environment)`**: Statically analyze and lint FiveM Lua scripts for security vulnerabilities (e.g. uncaptured `source`), performance anti-patterns (e.g. unthrottled `Wait(0)` loops), missing NUI `cb()` callbacks, and APISet execution mismatches.
- **`search_natives(query, namespace, apiset, limit)`**: Search FiveM / GTA V natives by name, hash, or description. Supports filtering by namespace (e.g. `PLAYER`, `VEHICLE`) and apiset (`all`, `client`, `server`).
- **`get_native_detail(name_or_hash)`**: Get full parameter types, return values, descriptions, and examples for a native.
- **`search_docs(query, limit)`**: Search curated FiveM developer guides (e.g. `fxmanifest`, `events`, `statebags`, `nui`).
- **`get_doc(topic)`**: Retrieve complete Markdown developer guide for a topic.
- **`ping(message)`**: Health check test tool.

### 📖 Resources
- **`docs://fivem/{topic}`**: Direct access to Markdown developer documentation (e.g. `docs://fivem/fxmanifest`, `docs://fivem/state-bags`).

### 💡 Prompts (10 Templates)
- **`scaffold_resource`**: Standard FiveM resource scaffolding template.
- **`scaffold_nui_resource`**: Complete NUI Web UI (React/Vue/HTML) resource template.
- **`scaffold_dui_screen`**: 3D In-game screen / billboard rendering resource template.
- **`scaffold_csharp_resource`**: .NET Standard C# `BaseScript` project template.
- **`scaffold_player_connecting`**: Connection deferrals, identifier validation, whitelist/ban checks.
- **`scaffold_onesync_spawner`**: Server-authoritative entity spawning with OneSync and routing buckets.
- **`scaffold_interaction_point`**: Dynamic sleep in-game interaction point with Marker, Blip, and key trigger.
- **`scaffold_damage_tracker`**: Low-level `gameEventTriggered` damage and kill tracking.
- **`scaffold_secure_event_handler`**: Secure server event handler with rate limiting and distance validation.
- **`scaffold_safe_transaction`**: Thread-safe authoritative economy transaction handler with mutex locking.

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
