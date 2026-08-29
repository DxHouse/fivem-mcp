from typing import Any
from fastmcp import FastMCP
from fivem_mcp.natives import natives_manager
from fivem_mcp.docs import docs_manager
from fivem_mcp.validator import script_validator

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
    Search FiveM developer guides, game reference constants, security architecture, and documentation.

    Args:
        query: Keywords to search for (e.g. 'sandbox', 'security', 'runtimes', 'controls', 'blips', 'events').
        limit: Maximum number of matching topics to return (default: 5).
    """
    return docs_manager.search(query, limit=limit)


@mcp.tool()
def get_doc(topic: str) -> str:
    """
    Retrieve the full Markdown developer guide for a specific FiveM topic.

    Args:
        topic: Topic slug or name (e.g. 'developers-sandbox', 'developers-script-runtimes', 'developers-server-security').
    """
    content = docs_manager.get_doc(topic)
    if not content:
        available = ", ".join(f"'{t['topic']}'" for t in docs_manager.list_topics())
        return f"Documentation topic '{topic}' not found. Available topics: {available}"
    return content


@mcp.tool()
def validate_script(code: str, environment: str = "auto") -> dict[str, Any]:
    """
    Statically analyze and lint FiveM Lua scripts for security vulnerabilities, performance anti-patterns, missing NUI callbacks, and native execution mismatches.

    Args:
        code: Lua source code to analyze.
        environment: Execution environment: 'auto' (detect from code), 'client', or 'server'. Defaults to 'auto'.
    """
    return script_validator.validate(code, environment=environment)


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
# MCP Prompts & Templates
# ============================================================================

@mcp.prompt()
def scaffold_resource(
    name: str,
    description: str = "",
    has_client: bool = True,
    has_server: bool = True,
    has_ui: bool = False,
) -> str:
    """Generate instructions and templates to scaffold a standard FiveM resource."""
    clean_desc = description or f"A modern FiveM resource for {name}"
    manifest_client = "    'client/*.lua',\n" if has_client else ""
    manifest_server = "    'server/*.lua',\n" if has_server else ""
    manifest_ui_file = "    'web/dist/index.html',\n    'web/dist/assets/*.*',\n" if has_ui else ""
    manifest_ui_page = "ui_page 'web/dist/index.html'\n" if has_ui else ""

    return f"""Please scaffold a standard, production-ready FiveM resource named `{name}`.

### Manifest (`fxmanifest.lua`):
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
"""


@mcp.prompt()
def scaffold_nui_resource(
    name: str,
    description: str = "",
    framework: str = "vanilla-html",
) -> str:
    """Generate a complete FiveM NUI Web UI resource template with message envelopes and callbacks."""
    clean_desc = description or f"A modern NUI Web UI resource for {name}"
    return f"""Please scaffold a production-ready FiveM NUI resource named `{name}` ({framework}).

### File Structure:
- `fxmanifest.lua` (with `ui_page 'web/dist/index.html'` and `files {{ 'web/dist/**' }}`)
- `config.lua`
- `client/main.lua` (NUI focus handling, `SendNUIMessage`, and `RegisterNUICallback`)
- `server/main.lua` (Authoritative event validation)
- `web/dist/index.html` (NUI HTML interface with message listeners)
- `web/dist/script.js` (Message envelope handler with `GetParentResourceName()`)
"""


@mcp.prompt()
def scaffold_dui_screen(
    name: str,
    url: str = "https://www.youtube.com",
    target_model: str = "prop_tv_flat_01",
    render_target: str = "tvscreen",
) -> str:
    """Generate a Direct-Rendered UI (DUI) resource template to project a web page onto a 3D in-game prop."""
    return f"""Please scaffold a FiveM DUI 3D Screen resource named `{name}`.

### Configuration:
- **Target Prop Model:** `{target_model}`
- **Render Target Name:** `{render_target}`
- **Default Web URL:** `{url}`

### Requirements:
1. Client script must create DUI with `CreateDui('{url}', 1280, 720)` and runtime texture dictionary.
2. Link render target to model using `RegisterNamedRendertarget('{render_target}', false)` and `LinkNamedRendertarget(`{target_model}`)`.
3. Render loop drawing `DrawSprite` onto the active render target with `SetTextRenderId`.
4. Resource stop cleanup handler calling `DestroyDui(duiObject)` to prevent GPU memory leaks.
"""


@mcp.prompt()
def scaffold_csharp_resource(
    name: str,
    description: str = "",
) -> str:
    """Generate a modern .NET C# FiveM resource template with BaseScript, EventHandlers, and .csproj."""
    clean_desc = description or f"A C# .NET FiveM resource for {name}"
    return f"""Please scaffold a .NET C# FiveM resource named `{name}`.

### Requirements:
1. **Client Project (`Client/{name}.Client.csproj`)**:
   - `TargetFramework: netstandard2.0`
   - `PackageReference: CitizenFX.Core.Client`
   - `TargetName: {name}.Client.net`

2. **Server Project (`Server/{name}.Server.csproj`)**:
   - `TargetFramework: netstandard2.0`
   - `PackageReference: CitizenFX.Core.Server`
   - `TargetName: {name}.Server.net`

3. Implement `ClientMain : BaseScript` with `EventHandlers` and `Tick += OnTick;` async task loops.
"""


@mcp.prompt()
def scaffold_player_connecting(
    name: str = "auth-deferrals",
) -> str:
    """Generate a production-ready FiveM player connection deferral handler with whitelist and identifier checks."""
    return f"""Please scaffold a FiveM connection deferrals resource named `{name}`.

### Requirements:
1. Handle `playerConnecting(playerName, setKickReason, deferrals)` event on the server.
2. Call `deferrals.defer()`, yield with `Wait(0)`, and display progress with `deferrals.update(...)`.
3. Extract player identifiers using `GetPlayerIdentifiers(src)` and verify Rockstar License (`license:`).
4. Provide structured error reject messages via `deferrals.done('Reason')` and approve via `deferrals.done()`.
5. Support adaptive card / presentation UI during queue or verification.
"""


@mcp.prompt()
def scaffold_onesync_spawner(
    name: str = "onesync-spawner",
    entity_type: str = "automobile",
) -> str:
    """Generate a OneSync server-authoritative entity spawning and routing bucket management resource."""
    return f"""Please scaffold a server-authoritative OneSync entity manager named `{name}`.

### Requirements:
1. Server script spawns entities using `CreateVehicleServerSetter(model, '{entity_type}', x, y, z, heading)`.
2. Wait for `DoesEntityExist(entity)` and retrieve synchronized `NetworkGetNetworkIdFromEntity(entity)`.
3. Support virtual world isolation using `SetPlayerRoutingBucket(src, bucketId)` and `SetEntityRoutingBucket(entity, bucketId)`.
4. Provide clean client-side event triggers to request and receive spawned network IDs.
"""


@mcp.prompt()
def scaffold_interaction_point(
    name: str = "custom-shop",
    marker_type: int = 1,
    blip_sprite: int = 52,
    key_bind: str = "E",
) -> str:
    """Generate a high-performance in-game interaction point with dynamic sleep interval, Marker, Blip, and 3D prompt."""
    return f"""Please scaffold an optimized client interaction point resource named `{name}`.

### Requirements:
1. **Minimap Blip:** Created with `AddBlipForCoord`, sprite `{blip_sprite}`, short range `true`.
2. **Dynamic Sleep Loop:**
   - When distance > 15.0m: Sleep for `1000` ms (0.00 ms CPU impact).
   - When distance <= 15.0m: Sleep for `0` ms and render `DrawMarker({marker_type}, ...)`.
   - When distance <= 2.0m: Display help text (~INPUT_CONTEXT~ to interact) and listen for `IsControlJustPressed(0, 38)`.
3. Action execution handler when player presses [{key_bind}].
"""


@mcp.prompt()
def scaffold_damage_tracker(
    name: str = "damage-logger",
) -> str:
    """Generate an event-driven damage and kill tracking script using GTA V's native CEventNetworkEntityDamage."""
    return f"""Please scaffold a client/server damage & combat logging resource named `{name}`.

### Requirements:
1. Client listens to `gameEventTriggered` for `CEventNetworkEntityDamage`.
2. Extract victim (`args[1]`), attacker (`args[2]`), fatal flag (`args[6] == 1`), and weapon hash (`args[7]`).
3. Check if victim is `PlayerPedId()`, resolve attacker player name if attacker is a player ped.
4. Dispatch structured client-to-server event `TriggerServerEvent('combat:onPlayerDamage', ...)` with weapon hash mapping.
"""


@mcp.prompt()
def scaffold_secure_event_handler(
    name: str = "secure-reward",
    cooldown_ms: int = 3000,
    max_distance: float = 5.0,
) -> str:
    """Generate a highly secure server event handler with source isolation, rate limiting, and coordinate distance verification."""
    return f"""Please scaffold a secure FiveM server-side event handler named `{name}`.

### Security Requirements:
1. **Source Isolation:** Immediately capture `local src = source` in the handler closure.
2. **Rate Limiting:** Enforce a per-player cooldown of `{cooldown_ms}` ms using `GetGameTimer()`.
3. **Distance Verification:** Verify player ped coordinates `GetEntityCoords(GetPlayerPed(src))` are within `{max_distance}` meters of the action location.
4. **Exploit Defense:** Log suspicious triggers or drop players with `DropPlayer(src, "Exploit attempt detected.")` if distance checks fail.
"""


@mcp.prompt()
def scaffold_safe_transaction(
    name: str = "economy-transaction",
) -> str:
    """Generate a race-condition immune, authoritative server transaction handler with player mutex locking."""
    return f"""Please scaffold a thread-safe server economy transaction handler named `{name}`.

### Requirements:
1. Use an in-memory transaction lock table (`transactionLocks[src] = true`) to prevent concurrent duplicate payouts.
2. Verify player wallet/inventory state authority on the server before mutating database or state bags.
3. Use `pcall` or structured `finally` blocks to guarantee `transactionLocks[src] = nil` is always released on error.
4. Log all successful and failed transactions with timestamp and rockstar license identifier.
"""


def main() -> None:
    """Entry point for the FiveM MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
