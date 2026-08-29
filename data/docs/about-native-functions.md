---
title: "FiveM Native Functions Guide"
description: "Calling conventions, pointer multiple return values, hashes, and namespaces for FiveM C++ game natives."
keywords: ["natives", "pointers", "hashes", "namespaces", "calling conventions", "cfx", "citizenfx"]
---

# FiveM Native Functions Guide

Native functions are C++ game engine functions exposed by FiveM and GTA V for scripting execution.

## 1. Quick Reference & Anatomy

| Component | Description | Example |
| :--- | :--- | :--- |
| **Name** | Human-readable identifier | `GET_PLAYER_PED`, `SET_ENTITY_COORDS` |
| **Hash** | 64-bit hex hash in game binary | `0x43A66C31C68491C0` |
| **Namespace** | Subsystem category | `PLAYER`, `VEHICLE`, `ENTITY`, `CFX` |
| **APISet** | Execution context | `client`, `server`, `shared` |

## 2. Production Code Examples

### Lua Calling Convention & Pointer Return Values
In Lua, native functions can be called in `PascalCase`, `camelCase`, or `ALL_CAPS`. Pointer parameters are automatically unpacked into multiple return values:

```lua
-- Ground Z check unpacking boolean success and float groundZ pointer:
local coords = GetEntityCoords(PlayerPedId())
local success, groundZ = GetGroundZFor_3dCoord(coords.x, coords.y, coords.z, false)
if success then
    print(string.format("Ground Z level is: %.2f", groundZ))
end
```

### C# Strongly-Typed Invocation
```csharp
using CitizenFX.Core;
using static CitizenFX.Core.Native.API;

int playerPed = GetPlayerPed(-1);
Vector3 coords = GetEntityCoords(playerPed, true);
```

## 3. Pitfalls & Best Practices

- **Never call natives in unthrottled loops:** Continuous `GetEntityCoords` or `DrawMarker` calls without `Wait(0)` or dynamic intervals cause frame rate drops.
- **Check Entity Existence:** Always run `DoesEntityExist(entity)` before reading entity natives to avoid nil handle crashes.
