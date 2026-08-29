from typing import Any
from fastmcp import FastMCP
from fivem_mcp.natives import natives_manager

mcp = FastMCP("fivem-mcp")


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
        limit: Maximum number of results to return (default: 10, max: 50).
    """
    safe_limit = max(1, min(limit, 50))
    return natives_manager.search(
        query=query,
        namespace=namespace,
        apiset=apiset,
        limit=safe_limit,
    )


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


def main() -> None:
    """Entry point for the FiveM MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
