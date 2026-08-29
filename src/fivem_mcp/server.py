from typing import Any
from fastmcp import FastMCP
from fivem_mcp.natives import natives_manager
from fivem_mcp.docs import docs_manager

mcp = FastMCP("fivem-mcp")


# ============================================================================
# Core Tools
# ============================================================================

@mcp.tool()
def ping(message: str = "pong") -> str:
    """A minimal test tool returning a pong response."""
    return f"pong: {message}"


@mcp.tool()
def search_natives(
    query: str,
    namespace: str | None = None,
    apiset: str = "all",
    limit: int = 10,
) -> list[dict[str, Any]]:
    """
    Search FiveM / GTA V native functions.

    Args:
        query: Search term to match against function name, hash, or description.
        namespace: Optional namespace filter (e.g. 'PLAYER', 'VEHICLE', 'ENTITY', 'CFX').
        apiset: Filter by execution environment: 'all', 'client', or 'server'. Defaults to 'all'.
        limit: Maximum number of results to return (default: 10).
    """
    return natives_manager.search(query, namespace=namespace, apiset=apiset, limit=limit)


@mcp.tool()
def get_native_detail(name_or_hash: str) -> dict[str, Any] | str:
    """
    Retrieve full details, parameter types, return values, and docstrings for a specific FiveM native.

    Args:
        name_or_hash: Function name (e.g. 'GET_PLAYER_PED') or hash (e.g. '0x43EB59F811F523C7').
    """
    detail = natives_manager.get_detail(name_or_hash)
    if not detail:
        return f"Native function '{name_or_hash}' not found."
    return detail


@mcp.tool()
def search_docs(query: str, limit: int = 5) -> list[dict[str, Any]]:
    """
    Search FiveM developer guides and architectural documentation.

    Args:
        query: Keywords to search for (e.g. 'fxmanifest', 'state bags', 'nui callbacks', 'events').
        limit: Maximum number of matching topics to return (default: 5).
    """
    return docs_manager.search(query, limit=limit)


@mcp.tool()
def get_doc(topic: str) -> str:
    """
    Retrieve the full Markdown developer guide for a specific FiveM topic.

    Args:
        topic: Topic slug or name (e.g. 'fxmanifest', 'networking-events', 'state-bags', 'nui-messages', 'performance-best-practices').
    """
    content = docs_manager.get_doc(topic)
    if not content:
        available = ", ".join(f"'{t['topic']}'" for t in docs_manager.list_topics())
        return f"Documentation topic '{topic}' not found. Available topics: {available}"
    return content


# ============================================================================
# MCP Resources
# ============================================================================

@mcp.resource("docs://fivem/{topic}")
def get_fivem_doc_resource(topic: str) -> str:
    """Expose FiveM Markdown developer guides as readable MCP resources."""
    content = docs_manager.get_doc(topic)
    if not content:
        return f"# Topic Not Found\n\nNo guide found for `{topic}`."
    return content


# ============================================================================
# MCP Prompts
# ============================================================================

@mcp.prompt()
def scaffold_resource(
    name: str,
    description: str = "",
    has_client: bool = True,
    has_server: bool = True,
    has_ui: bool = False,
) -> str:
    """
    Generate instructions and templates to scaffold a production-ready FiveM resource.

    Args:
        name: Name of the FiveM resource (kebab-case, e.g. 'custom-garage').
        description: Brief explanation of the resource's purpose.
        has_client: Include client-side Lua script directory and entry points.
        has_server: Include server-side Lua script directory and entry points.
        has_ui: Include NUI HTML/JS/CSS assets and manifest wiring.
    """
    clean_desc = description or f"A modern FiveM resource for {name}"
    
    manifest_client = "    'client/*.lua',\n" if has_client else ""
    manifest_server = "    'server/*.lua',\n" if has_server else ""
    manifest_ui_file = "    'web/dist/index.html',\n    'web/dist/assets/*.*',\n" if has_ui else ""
    manifest_ui_page = "ui_page 'web/dist/index.html'\n" if has_ui else ""

    return f"""Please scaffold a standard, production-ready FiveM resource named `{name}`.

### Resource Metadata
- **Name:** {name}
- **Description:** {clean_desc}
- **Lua Version:** 5.4 (`lua54 'yes'`)
- **FX Version:** `cerulean`
- **Target Game:** `gta5`

### Requirements
1. **`fxmanifest.lua`**:
```lua
fx_version 'cerulean'
game 'gta5'

name '{name}'
description '{clean_desc}'
version '1.0.0'
lua54 'yes'

shared_scripts {{
    'config.lua',
}}

client_scripts {{
{manifest_client}}}

server_scripts {{
{manifest_server}}}

files {{
{manifest_ui_file}}}

{manifest_ui_page}
```

2. **File Structure**:
- `config.lua` (Standard Config table)
{'- `client/main.lua` (Event handlers and game logic)' if has_client else ''}
{'- `server/main.lua` (Authoritative server events with source validation)' if has_server else ''}
{'- `web/dist/index.html` (NUI message passing & callback endpoints)' if has_ui else ''}

Please write the clean boilerplate files following FiveM performance best practices (dynamic sleep intervals in loops, cached entity handles, secure event source checks).
"""


def main() -> None:
    """Entry point for the FiveM MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
