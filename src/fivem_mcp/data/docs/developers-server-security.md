---
title: "Secure Your Events: FiveM Server Security Architecture"
description: "Authoritative server validation, trust boundaries, source verification, rate limiting, and exploit defense."
keywords: ["server security", "security", "source", "rate limiting", "distance check", "anticheat", "exploits", "trust boundary"]
---

# Secure Your Events: FiveM Server Security Architecture

In FiveM, the client runtime is untrusted. Malicious players can use Lua executors to invoke any `RegisterNetEvent` with arbitrary arguments. All authoritative logic, money awards, and item grants MUST be validated on the server.

## 1. Quick Reference & Core Rules

| Rule | Vulnerability Prevented | Implementation |
| :--- | :--- | :--- |
| **Source Isolation** | Identity spoofing | Capture `local src = source` immediately |
| **Distance Verification** | Remote teleport triggers | Compare `GetEntityCoords(GetPlayerPed(src))` with location |
| **Rate Limiting** | Event spamming / item duping | Per-player cooldown tracker with `GetGameTimer()` |

## 2. Production Code Examples

```lua
local playerCooldowns = {}
local shopCoords = vector3(25.0, -1345.0, 29.5)

RegisterNetEvent('shop:purchaseItem', function(itemId)
    local src = source
    local now = GetGameTimer()
    
    -- 1. Rate Limiting Check (2-second cooldown)
    if (now - (playerCooldowns[src] or 0)) < 2000 then return end
    playerCooldowns[src] = now

    -- 2. Distance Verification (max 5.0 meters)
    local ped = GetPlayerPed(src)
    local coords = GetEntityCoords(ped)
    if #(coords - shopCoords) > 5.0 then
        DropPlayer(src, "Exploit detected: Distance check failed.")
        return
    end

    -- 3. Authoritative server transaction
end)
```

## 3. Pitfalls & Best Practices

- **Never Trust Client Arguments for Price or Quantity:** Always fetch item prices and player account balances directly on the server.
