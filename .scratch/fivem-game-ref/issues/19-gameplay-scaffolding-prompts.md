# 19: FastMCP Gameplay Scaffolding Prompts Integration

**What to build:** Add gameplay scaffolding prompts (`scaffold_interaction_point`, `scaffold_damage_tracker`) to `src/fivem_mcp/server.py` and verify all 30 doc topics resolve via `docs://fivem/{topic}` resources.

**Blocked by:** 18: Game References Batch 2 (Weapons, Peds, Audio, World Zones, Game Events)

**Status:** ready-for-agent

- [x] `@mcp.prompt("scaffold_interaction_point")` implemented with dynamic sleep loop and marker/blip/prompt rendering
- [x] `@mcp.prompt("scaffold_damage_tracker")` implemented with `gameEventTriggered` damage and kill tracking
- [x] FastMCP CLI inspection validates all 8 prompts and all resource templates
