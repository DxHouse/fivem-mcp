from fastmcp import FastMCP

mcp = FastMCP("fivem-mcp")


@mcp.tool()
def ping(message: str = "pong") -> str:
    """A minimal test tool returning a pong response."""
    return f"pong: {message}"


def main() -> None:
    """Entry point for the FiveM MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
