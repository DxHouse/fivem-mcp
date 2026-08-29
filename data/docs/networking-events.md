---
title: "FiveM Networking & Client-Server Events Guide"
description: "Network event dispatching, client/server triggers, payload security, and latent events in FiveM."
keywords: ["networking", "events", "triggerclientevent", "triggerserverevent", "registernetevent", "latent events", "security"]
---

# FiveM Networking & Client-Server Events Guide

In FiveM, communication between the game client and FXServer occurs over an event-driven network architecture.

## 1. Quick Reference

| Function | Direction | Description |
| :--- | :--- | :--- |
| `RegisterNetEvent(name, handler)` | Shared | Marks an event as callable over the network |
| `TriggerServerEvent(name, ...)` | Client -> Server | Dispatches an event from client to server |
| `TriggerClientEvent(name, target, ...)` | Server -> Client | Dispatches an event from server to player |
| `TriggerLatentClientEvent(...)` | Server -> Client | Sends large payloads with bandwidth rate limiting |

## 2. Production Code Examples

```lua
-- SERVER SIDE: Authoritative Handler
RegisterNetEvent('inventory:buyItem', function(itemId, count)
    local src = source -- ALWAYS capture source immediately
    -- authoritative deduction and reward
    TriggerClientEvent('inventory:onItemBought', src, itemId, count)
end)
```

## 3. Pitfalls & Best Practices

- **Never Trust Client Arguments:** Never accept client-provided player IDs, bank balances, or prices in server event parameters.
