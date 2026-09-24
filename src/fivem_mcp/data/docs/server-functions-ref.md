---
title: "Server-Side Scripting Functions Reference"
description: "Server runtime functions for player lifecycle management, HTTP requests, ACE permissions, and identifiers."
keywords: ["server functions", "getplayers", "dropplayer", "performhttprequest", "isplayeraceallowed", "getplayeridentifiers", "admin", "permissions"]
---

# Server-Side Scripting Functions Reference

FXServer provides server-side runtime functions for player lifecycle management, HTTP requests, ACE permissions, and console commands.

## 1. Quick Reference

| Function | Description |
| :--- | :--- |
| `GetPlayers()` | Returns array of string player source IDs |
| `GetPlayerIdentifiers(src)` | Returns array of platform IDs (license, discord, steam) |
| `DropPlayer(src, reason)` | Disconnects client with custom kick reason |
| `IsPlayerAceAllowed(src, obj)` | Checks ACE permission node |
| `PerformHttpRequest(url, cb, ...)` | Asynchronous HTTP client request |

## 2. Production Code Examples

```lua
-- Fetch player identifiers and verify license
local identifiers = GetPlayerIdentifiers(source)
for _, id in ipairs(identifiers) do
    if string.find(id, "license:") then
        print("Player License:", id)
    end
end

-- Asynchronous HTTP Request
PerformHttpRequest("https://api.github.com/zen", function(statusCode, responseText, headers)
    if statusCode == 200 then
        print("GitHub Zen:", responseText)
    end
end, "GET", "", { ["User-Agent"] = "FiveM-Server" })
```

## 3. Pitfalls & Best Practices

- **Never perform synchronous blocking I/O:** Always use `PerformHttpRequest` or async database libraries (`oxmysql`) to prevent freezing the server tick thread.
