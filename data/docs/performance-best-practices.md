---
title: "FiveM Performance Best Practices"
description: "Optimization techniques for Lua loops, thread sleeping, vector math caching, and resource cleanup."
keywords: ["performance", "optimization", "wait", "cpu time", "resmon", "profiling", "vector math", "cleanup"]
---

# FiveM Performance Best Practices

Maintaining high server tick rates and smooth 60+ client FPS requires efficient thread intervals and minimal tick loop overhead.

## 1. Quick Reference

| Technique | Anti-Pattern | Best Practice |
| :--- | :--- | :--- |
| **Thread Sleep** | `while true do Wait(0)` everywhere | Dynamic wait: `Wait(1000)` when far away, `Wait(0)` when close |
| **Distance Math** | `GetDistanceBetweenCoords(x1,y1,z1,x2,y2,z2,true)` | Length operator: `#(posA - posB)` |
| **Entity Lookup** | Repeated `GetPlayerPed(-1)` in loop | Cache `PlayerPedId()` once per tick |
| **Resource Stop** | Leaking blips, markers, DUI objects | Clean up state inside `onResourceStop` |

## 2. Production Code Examples

```lua
-- Dynamic Sleep Pattern (0.00 ms CPU impact when idle)
CreateThread(function()
    local shopCoords = vector3(25.0, -1345.0, 29.5)
    while true do
        local sleep = 1000
        local playerCoords = GetEntityCoords(PlayerPedId())
        local distance = #(playerCoords - shopCoords)

        if distance < 15.0 then
            sleep = 0
            DrawMarker(1, shopCoords.x, shopCoords.y, shopCoords.z - 1.0, 0, 0, 0, 0, 0, 0, 1.5, 1.5, 0.75, 255, 50, 50, 200, false, false, 2, false, nil, nil, false)
            if distance < 2.0 then
                -- Display prompt & handle input
            end
        end
        Wait(sleep)
    end
end)
```

## 3. Pitfalls & Best Practices

- **Never create runaway threads:** Loops spawned on every key press without exit conditions cause memory and CPU leaks.
