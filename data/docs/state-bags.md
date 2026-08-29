# FiveM StateBags Guide

StateBags provide synchronized key-value state storage across Client and Server for Entities, Players, and Global state. They replace heavy network event spam for tracking entity states (e.g. handcuffed, trunk open, faction).

## Types of StateBags

1. **GlobalState**: Shared globally across the whole server and all clients.
2. **Player(source).state**: State associated with a specific connected player.
3. **Entity(handle).state**: State attached to a networked game entity (Ped, Vehicle, Object).

## Reading and Writing State

```lua
-- ===================
-- SERVER SIDE
-- ===================

-- 1. Global State
GlobalState.isDoubleXP = true

-- 2. Player State
local playerState = Player(source).state
playerState:set('job', 'police', true) -- 3rd param (replicated=true) syncs to all clients

-- 3. Entity State
local vehicle = GetVehiclePedIsIn(GetPlayerPed(source), false)
Entity(vehicle).state:set('isFuelPumped', true, true)
```

```lua
-- ===================
-- CLIENT SIDE
-- ===================

-- Read state
local isDoubleXP = GlobalState.isDoubleXP
local myJob = LocalPlayer.state.job

-- Read entity state
local vehState = Entity(vehicle).state.isFuelPumped
```

## StateBag Change Handlers (Reactive Listeners)

Listen reactively whenever a state key changes:

```lua
-- Add a listener for any entity whose 'isFuelPumped' state changes
AddStateBagChangeHandler('isFuelPumped', nil, function(bagName, key, value, _reserved, replicated)
    local entity = GetEntityFromStateBagName(bagName)
    if entity and DoesEntityExist(entity) then
        print(string.format("Entity %s fuel status changed to: %s", entity, tostring(value)))
    end
end)
```

## StateBag Best Practices

- Use StateBags for **persistent attributes** rather than one-off actions.
- Only pass `replicated = true` when clients genuinely need to know the state (reduces network traffic).
