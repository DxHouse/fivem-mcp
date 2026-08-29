# FiveM Script Performance & Optimization Guide

FiveM scripts run continuously in the game loop. Unoptimized scripts cause frame drops (low client FPS) and server lag (hiccups in tick rate).

## Thread Management & Tick Rates

### ❌ Anti-Pattern: Tight Loops (`Wait(0)` without distance checks)

```lua
-- BAD: Runs every single game frame (~60-144 times/sec) regardless of distance
CreateThread(function()
    while true do
        Wait(0)
        local ped = PlayerPedId()
        local coords = GetEntityCoords(ped)
        DrawMarker(1, targetCoords.x, targetCoords.y, targetCoords.z, 0,0,0, 0,0,0, 1.0, 1.0, 1.0, 255,0,0,200, false, false, 2, false, nil, nil, false)
    end
end)
```

### ✅ Best Practice: Dynamic Sleep Intervals

```lua
-- GOOD: Sleeps 1000ms when far away, drops to Wait(0) only when player is nearby
CreateThread(function()
    while true do
        local sleep = 1000
        local ped = PlayerPedId()
        local coords = GetEntityCoords(ped)
        local dist = #(coords - targetCoords) -- Fast vector distance in Lua 5.4

        if dist < 20.0 then
            sleep = 0
            DrawMarker(1, targetCoords.x, targetCoords.y, targetCoords.z, 0,0,0, 0,0,0, 1.0, 1.0, 1.0, 255,0,0,200, false, false, 2, false, nil, nil, false)
            if dist < 1.5 then
                -- Show prompt
            end
        end

        Wait(sleep)
    end
end)
```

## Optimization Checklist

1. **Cache Local Handles:**
   - Instead of calling `PlayerPedId()` 10 times in a function, store `local ped = PlayerPedId()` once.
2. **Use Vector Math (`#` length operator):**
   - In Lua 5.4, `#(coordsA - coordsB)` is significantly faster than `GetDistanceBetweenCoords()`.
3. **Clean Up on Resource Stop:**
   - Always delete created blips, spawned peds, and remove state handlers when the resource stops:
   ```lua
   AddEventHandler('onResourceStop', function(resourceName)
       if GetCurrentResourceName() ~= resourceName then return end
       -- delete spawned objects/blips here
   end)
   ```
4. **Use ox_lib / Caching Helpers:**
   - Use `lib.points` or spatial grids instead of manual distance loop checks where possible.
