# FiveM Native API & Developer Documentation Context

Provides access, indexing, search, detailed inspection of FiveM and GTA V native functions, curated developer guides, Scripting Reference catalogs, Game Reference constant tables, developer architecture docs, and MCP resources for script development.

## Language

**Native**:
An engine or framework C++ function exposed to GTA V and FiveM scripting runtimes (Lua, JavaScript, C#).
_Avoid_: Native function, game function, API endpoint

**Hash**:
The unique 64-bit hexadecimal identifier (e.g. `0x43A66C31C68491C0`) representing a native function internally in the game binary.
_Avoid_: Function ID, native ID, hex code

**Namespace**:
A categorical grouping of related natives based on game subsystem (e.g., `PLAYER`, `VEHICLE`, `ENTITY`, `CFX`, `WEAPON`).
_Avoid_: Category, module, package

**APISet**:
The execution environment where a native is valid to run (`client`, `server`, or `shared`).
_Avoid_: Environment, side, runtime context

**Resource**:
A packaged FiveM module containing scripts, configuration, and assets managed by FXServer.
_Avoid_: Plugin, mod, addon, package

**Manifest**:
The `fxmanifest.lua` configuration file declaring resource metadata, script entry points, and asset dependencies.
_Avoid_: Config file, package.json, meta file

**StateBag**:
A synchronized, key-value state store attached to entities, players, or global server state.
_Avoid_: Sync table, shared variable, entity metadata

**Convar**:
A console variable in FXServer used for server configuration, feature toggling, and client replication.
_Avoid_: Config variable, server setting, env var

**OneSync**:
FiveM's custom multiplayer synchronization engine supporting high player counts, server-side entity creation, and spatial culling.
_Avoid_: Sync engine, netcode, server sync

**RoutingBucket**:
A virtual world / dimension index in OneSync isolating players and entities from other buckets.
_Avoid_: Dimension, virtual world, instance

**Deferrals**:
A connection handshake mechanism allowing server scripts to pause player connection, display adaptive cards, and verify whitelists.
_Avoid_: Connection hook, queue system, login check

**AcePermission**:
An Access Control Entry permission node (e.g. `command.kick`, `group.admin`) evaluated by FXServer.
_Avoid_: Admin level, user rank, permission role

**Identifier**:
A player's unique authentication string (e.g. `license:xxx`, `discord:xxx`, `steam:xxx`).
_Avoid_: Account ID, user identifier, player GUID

**GameEvent**:
A low-level C++ game engine event (e.g. `CEventNetworkEntityDamage`) caught via `gameEventTriggered`.
_Avoid_: Engine event, damage signal

**Blip**:
A 2D radar / minimap waypoint icon and label rendered in the GTA V HUD.
_Avoid_: Map icon, radar pin, minimap marker

**Marker**:
A 3D geometric shape (cylinder, chevron, ring) drawn in the game world with `DrawMarker`.
_Avoid_: 3D ring, checkpoint circle, ground light

**ControlAction**:
A numerical input index (0-357) mapping to keyboard, mouse, or controller buttons.
_Avoid_: Key code, button ID, input number

**HUDColor**:
A standard GTA V HUD palette color index (e.g. `HUD_COLOUR_RED`) or embedded color token (`~r~`).
_Avoid_: Text color, UI tint

**GamerTag**:
An overhead player name tag and health indicator managed via `CreateMpGamerTag`.
_Avoid_: Nameplate, overhead text

**Zone**:
A named GTA V geographical region identified by a 3-letter uppercase code (e.g. `AIRP`, `DOWNT`).
_Avoid_: Map region, neighborhood code

**Sandbox**:
The isolated execution environment in FiveM preventing unauthorized client-side file system and OS access.
_Avoid_: Security jail, VM layer

**Msgpack**:
The MessagePack binary serialization format used to transport data across different FiveM script runtimes and network events.
_Avoid_: Binary JSON, serialization buffer

**TrustBoundary**:
The strict separation between untrusted client game instances and authoritative FXServer daemons.
_Avoid_: Security wall, client trust

**RateLimiter**:
A per-player cooldown tracker mitigating event spam and race-condition exploitation.
_Avoid_: Flood gate, spam filter

**NUI**:
Native User Interface; an embedded Chromium web view rendering HTML/CSS/JS inside the game client.
_Avoid_: Webview, CEF, HTML UI

**DUI**:
Direct-Rendered User Interface; an in-game Chromium browser view rendered dynamically onto 3D game meshes and textures.
_Avoid_: In-game browser, web screen, 3d nui

**Scaleform**:
Autodesk Scaleform GFx Flash-based user interface system used by GTA V for minimaps, instructional buttons, and HUD elements.
_Avoid_: Flash UI, gfx movie

**Submix**:
An audio routing bus in FiveM's Mumble audio pipeline used to apply spatial filters, radio distortion, or megaphone effects.
_Avoid_: Voice filter, audio effect

**Collection**:
A structured asset grouping for drawable clothing components and character customization props in modern GTA V builds.
_Avoid_: Clothes pack, prop set

**NetworkId**:
A synchronized unique integer identifier assigned to a networked entity across the server and all connected clients.
_Avoid_: Global entity ID, net handle

**LocalHandle**:
An integer index representing an entity locally on a single game client or server instance.
_Avoid_: Entity ID, ped index, vehicle number

**Profiler**:
FiveM's built-in frame-by-frame performance recording tool used for CPU tick analysis and Chrome Tracing.
_Avoid_: Lag detector, fps meter

**Event**:
An asynchronous message dispatched between client and server runtimes or within the same runtime.
_Avoid_: Signal, RPC, message packet

**Client**:
The FiveM game instance running on the player machine executing client-side scripts.
_Avoid_: Frontend, player client

**Server**:
The FiveM server daemon (FXServer) executing server-side authoritative scripts.
_Avoid_: Backend, host, FXServer

**Signature**:
The formal declaration of a native including its name, ordered typed parameters, and return type.
_Avoid_: Declaration, prototype, function definition

**ScriptValidator**:
A static analysis rule engine that audits FiveM Lua scripts for security leaks, performance bottlenecks, and native APISet mismatches.
_Avoid_: Code checker, lua parser

**StaticLinter**:
The diagnostic linter component verifying NUI callbacks, source closures, and tight loop throttling.
_Avoid_: Error scanner, code cleaner

**NodeWrapper**:
A lightweight npm executable package (@dxhouse/fivem-mcp) enabling one-command execution via npx.
_Avoid_: Node bridge, JS server, npm adapter

**UvxRunner**:
The ephemeral tool launcher executing fivem-mcp directly from Git or PyPI in an isolated Python environment.
_Avoid_: Python runner, package exec, pipx tool

