# Scripting in Lua (Lua 5.4 Runtime)

FiveM supports modern Lua 5.4 with native vector math, integers, bitwise operators, and scoped resource environments.

## Lua 5.4 Features in FiveM

Always enable Lua 5.4 in `fxmanifest.lua`:
```lua
lua54 'yes'
```

### 1. Vector Types (`vector2`, `vector3`, `vector4`)
FiveM embeds native C vector types directly into the Lua runtime:

```lua
local posA = vector3(100.0, -200.0, 30.0)
local posB = GetEntityCoords(PlayerPedId())

-- Distance calculation using length operator (#)
local distance = #(posA - posB)

-- Vector arithmetic
local spawnPos = posA + vector3(0.0, 0.0, 1.0)
```

### 2. Thread Scheduling (`Citizen.CreateThread` / `CreateThread`)
Threads in FiveM are cooperative coroutines managed by the game scheduler:

```lua
CreateThread(function()
    while true do
        Wait(500) -- Pauses coroutine execution without blocking the main game frame
        -- background task logic
    end
end)
```

### 3. Global & Resource Scoping
- Each resource executes inside its own isolated `_G` global table.
- Scripts in the same resource share globals.
- Cross-resource communication is done via **Exports** or **Events**:

```lua
-- Resource A: Export a function
exports('calculateTax', function(amount)
    return amount * 0.07
end)

-- Resource B: Call the exported function
local tax = exports['resource-a']:calculateTax(500)
```
