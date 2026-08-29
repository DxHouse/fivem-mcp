# 07: FastMCP Tools, Resources & Scaffolding Prompt Integration

**What to build:** Integrate `DocsManager` into the FastMCP server, adding `search_docs` and `get_doc` tools, registering `@mcp.resource("docs://fivem/{topic}")` URI endpoints, and implementing `@mcp.prompt("scaffold_resource")` for standard FiveM resource scaffolding.

**Blocked by:** 06: In-Memory Docs Search Engine (DocsManager)

**Status:** ready-for-agent

- [x] `search_docs` and `get_doc` tools registered in FastMCP server
- [x] `@mcp.resource("docs://fivem/{topic}")` provides direct Markdown document access
- [x] `@mcp.prompt("scaffold_resource")` generates production-ready FiveM resource templates
- [x] FastMCP CLI inspection validates tools, resources, and prompts
