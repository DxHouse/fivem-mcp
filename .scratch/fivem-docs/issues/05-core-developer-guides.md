# 05: Core Developer Guides & Markdown Docs Content

**What to build:** Create curated FiveM developer guides in `data/docs/` covering `fxmanifest.lua`, client-server event networking, StateBags, NUI message passing, and tick-rate performance optimization. Update `CONTEXT.md` with new domain terms and record architectural decision in `docs/adr/0002-markdown-docs-and-resources.md`.

**Blocked by:** None (can start immediately)

**Status:** ready-for-agent

- [x] `data/docs/fxmanifest.md` contains full manifest directives and configuration examples
- [x] `data/docs/networking-events.md` covers event triggers, listeners, payload security, and latent events
- [x] `data/docs/state-bags.md` covers Entity/Player/Global StateBags and change handlers
- [x] `data/docs/nui-messages.md` covers NUI message passing, callbacks, and focus management
- [x] `data/docs/performance-best-practices.md` covers thread ticks, wait intervals, and cleanup
- [x] `CONTEXT.md` updated with `Resource`, `Manifest`, `StateBag`, `NUI`, and `Event`
- [x] `docs/adr/0002-markdown-docs-and-resources.md` records documentation format and MCP exposure decisions
