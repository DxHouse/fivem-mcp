# FiveM Developer Documentation Knowledge Base

Comprehensive catalog of 33 curated developer guides, architectural manuals, and GTA V constant references for FiveM script development.

---

## 🛡️ Developer Docs & Security Architecture
- [developers-sandbox.md](developers-sandbox.md) — Client/server security sandbox, filesystem restrictions, and Resource KVP.
- [developers-script-runtimes.md](developers-script-runtimes.md) — Lua 5.4, V8, C# Mono internals, memory models, and `msgpack` export serialization overhead.
- [developers-server-security.md](developers-server-security.md) — Server security, trust boundaries, `source` verification, rate limiting, and distance validation.

---

## 📜 Scripting Reference & Subsystems
- [client-functions-ref.md](client-functions-ref.md) — Client runtime functions, `RegisterKeyMapping`, `LocalPlayer`, C# wrappers.
- [server-functions-ref.md](server-functions-ref.md) — Server runtime functions, `GetPlayers`, `DropPlayer`, `PerformHttpRequest`, `IsPlayerAceAllowed`.
- [events-catalog.md](events-catalog.md) — Built-in client/server event schemas (`playerConnecting` deferrals, `playerDropped`, `playerSpawned`).
- [convars.md](convars.md) — Server ConVars, replication (`setr`), server info (`sets`), `server.cfg` directives.
- [onesync-routing-buckets.md](onesync-routing-buckets.md) — OneSync Infinity, `CreateVehicleServerSetter`, `SetPlayerRoutingBucket`.
- [fxmanifest.md](fxmanifest.md) — Comprehensive `fxmanifest.lua` directive reference table.
- [nui-messages.md](nui-messages.md) — NUI Chromium web view message envelopes, callbacks, and focus management.

---

## 🎮 Game References & Constants
- [game-references-controls.md](game-references-controls.md) — Control action IDs (0-357), input groups, and `DisableControlAction`.
- [game-references-blips-markers.md](game-references-blips-markers.md) — Minimap blip sprites, colors, 3D world marker types (0-43), and checkpoints.
- [game-references-ui-hud.md](game-references-ui-hud.md) — HUD colors, text formatting tokens (`~r~`, `~g~`, `~h~`), and Gamer Tags.
- [game-references-vehicles.md](game-references-vehicles.md) — Vehicle models by category, paint color IDs (0-159), and handling flags.
- [game-references-weapons-peds.md](game-references-weapons-peds.md) — Weapon hashes, ped models, and pickup hashes.
- [game-references-audio-speech.md](game-references-audio-speech.md) — Radio stations, ambient speeches, ped voice names, and soundsets.
- [game-references-world-zones.md](game-references-world-zones.md) — GTA V Map Zones (3-letter codes to full names), Profile Settings, Data Files.
- [game-references-game-events.md](game-references-game-events.md) — Low-level `gameEventTriggered` events (`CEventNetworkEntityDamage`).

---

## 📖 Core Manual & Runtimes
- [about-native-functions.md](about-native-functions.md) — Native calling conventions, pointer return values, hashes, and namespaces.
- [runtimes-lua.md](runtimes-lua.md) — Modern Lua 5.4 runtime, native vector arithmetic, and coroutine scheduling.
- [runtimes-csharp.md](runtimes-csharp.md) — .NET Standard C# scripting with `CitizenFX.Core`, `BaseScript`, and `.csproj`.
- [using-profiler.md](using-profiler.md) — FiveM Profiler (`profiler record`), `resmon 1`, and Speedscope tracing.
- [network-ids.md](network-ids.md) — Network ID vs Local Handle conversion and OneSync entity routing.
- [events-lifecycle.md](events-lifecycle.md) — Event listeners, `CancelEvent()`, payload validation, and latency.
- [dui-3d-screens.md](dui-3d-screens.md) — Direct-Rendered UI (`CreateDui`), and 3D in-game screen rendering.
- [loading-screens.md](loading-screens.md) — Custom loading screens, progress events, and manual shutdown.
- [voice-mumble.md](voice-mumble.md) — Built-in Mumble 3D spatial voice, proximity grids, and radio DSP submix filters.
- [scaleform.md](scaleform.md) — Scaleform Flash GFx movies, instructional buttons, and minimap HUD.
- [collections-and-props.md](collections-and-props.md) — Modern collection-based clothing components and props.
- [fuel-consumption.md](fuel-consumption.md) — Native FiveM vehicle fuel subsystem and consumption rate multipliers.
- [networking-events.md](networking-events.md) — Client/Server network event triggers and security.
- [state-bags.md](state-bags.md) — Entity, Player, and Global state synchronization.
- [performance-best-practices.md](performance-best-practices.md) — Thread management, vector math, and cleanup.
