---
title: "Client-Side Scripting Functions Reference"
description: "Client-side runtime functions, command helpers, key-mapping systems, and class wrappers for Lua and C#."
keywords: ["client functions", "registerkeymapping", "localplayer", "screen", "world", "game", "keybind", "input"]
---

# Client-Side Scripting Functions Reference

FiveM provides a suite of client-side runtime functions, command helpers, key-mapping systems, and class wrappers for Lua and C#.

## 1. Quick Reference

| Function / Wrapper | Runtime | Description |
| :--- | :--- | :--- |
| `RegisterKeyMapping(cmd, desc, pad, key)` | Shared | Registers a player-rebindable keybinding |
| `LocalPlayer.state` | Client Lua | Accesses local client's state bag |
| `Screen.ShowNotification(msg)` | Client C# | Displays standard GTA V left-side notification |
| `SetNuiFocus(hasCursor, hasKeyboard)` | Client Lua/JS | Sets input focus to NUI web view |

## 2. Production Code Examples

```lua
-- Rebindable key mapping (default 'TAB')
RegisterCommand('+openInventory', function()
    print("Opening inventory...")
end, false)
RegisterCommand('-openInventory', function()
    print("Closing inventory.")
end, false)

RegisterKeyMapping('+openInventory', 'Open Player Inventory', 'keyboard', 'TAB')
```

## 3. Pitfalls & Best Practices

- **Never Hardcode Fixed Key Presses:** Always use `RegisterKeyMapping` so players can customize keybindings in GTA V Settings without script edits.
