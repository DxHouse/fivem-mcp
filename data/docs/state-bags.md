---
title: "FiveM State Bags Guide"
description: "Synchronized key-value state replication on Entities, Players, and Global Server State with change handlers."
keywords: ["state bags", "statebags", "entity state", "player state", "globalstate", "addstatebagchangehandler", "sync"]
---

# FiveM State Bags Guide

State Bags provide automatic network replication for key-value pairs attached to Entities, Players, or the Global Server State.

## 1. Quick Reference

| State Bag Scope | Access Pattern | Sync Target |
| :--- | :--- | :--- |
| **GlobalState** | `GlobalState.weather = "RAIN"` | All connected clients |
| **Player State** | `Player(src).state.isDead = true` | Synced to all clients |
| **Entity State** | `Entity(veh).state.plate = "ABC"` | Synced to players in culling radius |

## 2. Production Code Examples

```lua
-- SERVER SIDE: Set player state
local playerState = Player(source).state
playerState:set('isHandcuffed', true, true) -- 3rd argument 'true' replicates to clients

-- CLIENT SIDE: Reactive change handler
AddStateBagChangeHandler('isHandcuffed', nil, function(bagName, key, value)
    local entity = GetEntityFromStateBagName(bagName)
    if entity == PlayerPedId() then
        print("Handcuff state updated to:", value)
    end
end)
```

## 3. Pitfalls & Best Practices

- **Avoid Over-Syncing:** Only set the 3rd parameter (`replicated`) to `true` when other clients actually need to know about the state.
