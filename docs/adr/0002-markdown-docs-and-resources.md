# 0002: Modular Markdown Guides & MCP Resources

We chose to store FiveM developer documentation as modular Markdown files in `data/docs/` and expose them through both MCP Tools (`search_docs`, `get_doc`) and MCP Resources (`docs://fivem/{topic}`). This separation allows human developers and contributors to edit guides as plain text while enabling AI agents to perform token-efficient searches or inspect complete reference topics directly through standard MCP URI schemes.
