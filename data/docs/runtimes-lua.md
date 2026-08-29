---
title: "Scripting in Lua (Lua 5.4 Runtime)"
description: "FiveM modern Lua 5.4 runtime, native vector arithmetic, thread scheduling, and scoped environments."
keywords: ["lua", "lua54", "vectors", "vector3", "vector2", "vector4", "createthread", "wait", "exports", "coords"]
---

# Scripting in Lua (Lua 5.4 Runtime)

FiveM supports modern Lua 5.4 with native vector math, 64-bit integers, bitwise operators, and isolated resource environments.

## 1. Quick Reference

| Feature | Syntax / Directive | Notes |
| :--- | :--- | :--- |
| **Enable Lua 5.4** | `lua54 'yes'` in `fxmanifest.lua` | Recommended for all modern resources |
| **Vector Types** | `vector2(x, y)`, `vector3(x, y, z)`, `vector4(x, y, z, w)` | Embedded C types with length operator `#` |
| **Coroutines** | `CreateThread(function() ... end)` | Non-blocking cooperative scheduler |
| **Yielding** | `Wait(ms)` | Pauses coroutine without blocking game frame |

## 2. Production Code Examples

### Vector Math & Distance Calculation
```lua
local spawnPos = vector3(100.0, -200.0, 30.0)
local playerPos = GetEntityCoords(PlayerPedId())

-- Distance calculation using length operator (#)
local distance = #(spawnPos - playerPos)

if distance < 5.0 then
    print("Player is within 5 meters of spawn.")
end
```

### Resource Exports
```lua
-- Resource A (Defines export):
exports('calculatePrice', function(base, tax)
    return base * (1 + tax)
end)

-- Resource B (Calls export):
local total = exports['resource-a']:calculatePrice(100, 0.07)
```

## 3. Pitfalls & Best Practices

- **Avoid Global Pollution:** Always declare variables with `local` to prevent leaking state across resource scripts.
- **Dynamic Thread Sleep:** Never use `while true do Wait(0)` when player is far away from an interaction point; sleep for `500` or `1000` ms dynamically.
