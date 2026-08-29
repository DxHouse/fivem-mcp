---
title: "FiveM Standard Built-in Events Catalog"
description: "Catalog of official FiveM built-in client and server events with exact parameter schemas and handlers."
keywords: ["events catalog", "playerconnecting", "playerdropped", "playerspawned", "gameeventtriggered", "deferrals", "builtin events"]
---

# FiveM Standard Built-in Events Catalog

Catalog of official FiveM built-in client and server events with exact parameter schemas and handlers.

## 1. Quick Reference & Event Matrix

| Event Name | Environment | Parameter Schema | Description |
| :--- | :--- | :--- | :--- |
| `playerConnecting` | Server | `(playerName, setKickReason, deferrals)` | Player initiating connection |
| `playerDropped` | Server | `(reason)` | Player disconnecting |
| `playerSpawned` | Client | `(spawnInfo)` | Player spawned by spawnmanager |
| `gameEventTriggered` | Client | `(name, argsTable)` | Low-level C++ game engine event |

## 2. Production Code Examples

```lua
-- Connection Deferrals Handling
AddEventHandler('playerConnecting', function(playerName, setKickReason, deferrals)
    local src = source
    deferrals.defer()
    Wait(0)
    deferrals.update("Verifying whitelist...")
    deferrals.done()
end)
```

## 3. Pitfalls & Best Practices

- **Always Call `Wait(0)` in Deferrals:** `deferrals.defer()` must yield with `Wait(0)` before calling `deferrals.update` or `deferrals.done`.
