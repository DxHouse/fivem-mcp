# Secure Your Events: FiveM Server Security Architecture

In FiveM, the client runtime is untrusted. Malicious players can use Lua executors to invoke any `RegisterNetEvent` with arbitrary arguments. All authoritative logic, money awards, and item grants MUST be validated on the server.

## Core Security Rules

### 1. Always Capture `source` Locally
Never trust a client-supplied player ID. Always use the implicit `source` global captured as a local variable inside the event handler:

```lua
-- SECURE:
RegisterNetEvent('bank:deposit', function(amount)
    local src = source -- Capture immediately!
    -- Authoritative server logic using src
end)

-- VULNERABLE (DO NOT DO THIS):
RegisterNetEvent('bank:deposit', function(playerId, amount)
    -- Modder can pass another player's ID!
end)
```

### 2. Distance Verification for World Actions
Before awarding items or money from a robbery or shop, verify that the player ped is physically near the shop coordinates:

```lua
local shopCoords = vector3(25.0, -1345.0, 29.5)
local maxDistance = 5.0

RegisterNetEvent('shop:purchaseItem', function(itemId)
    local src = source
    local ped = GetPlayerPed(src)
    local playerCoords = GetEntityCoords(ped)

    if #(playerCoords - shopCoords) > maxDistance then
        print(string.format("[SECURITY ALERT] Player %s triggered purchase from too far away!", src))
        DropPlayer(src, "Exploit attempt: Distance check failed.")
        return
    end

    -- Process purchase
end)
```

### 3. Per-Player Cooldowns & Rate Limiting
Prevent spamming event triggers to duplicate items:

```lua
local playerCooldowns = {}

RegisterNetEvent('mining:harvestRock', function()
    local src = source
    local now = GetGameTimer()
    local lastAction = playerCooldowns[src] or 0

    if (now - lastAction) < 3000 then -- 3 second cooldown
        return -- Ignore spam
    end
    playerCooldowns[src] = now

    -- Award mining rock
end)
```
