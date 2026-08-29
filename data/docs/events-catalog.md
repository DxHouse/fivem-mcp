# FiveM Standard Built-in Events Catalog

Catalog of official FiveM built-in client and server events with exact parameter schemas and handlers.

## Server-Side Built-in Events

### 1. `playerConnecting`
Fired when a player initiates connection to the server. Used for whitelisting, ban checks, and connection deferrals:

```lua
AddEventHandler('playerConnecting', function(playerName, setKickReason, deferrals)
    local src = source
    deferrals.defer()
    
    Wait(0) -- Mandatory yield before calling deferral methods
    deferrals.update(string.format("Hello %s, checking your whitelist status...", playerName))

    local identifiers = GetPlayerIdentifiers(src)
    local hasLicense = false
    for _, id in ipairs(identifiers) do
        if string.find(id, "license:") then hasLicense = true break end
    end

    if not hasLicense then
        deferrals.done("Connection rejected: Rockstar License identifier not found.")
        return
    end

    -- Allow connection
    deferrals.done()
end)
```

### 2. `playerJoining`
Fired when a player has completed deferrals and begins loading game assets:

```lua
AddEventHandler('playerJoining', function(oldID)
    local src = source
    print(string.format("Player %s is joining the game world.", src))
end)
```

### 3. `playerDropped`
Fired when a player disconnects from the server:

```lua
AddEventHandler('playerDropped', function(reason)
    local src = source
    local playerName = GetPlayerName(src)
    print(string.format("Player %s (%s) disconnected. Reason: %s", playerName, src, reason))
end)
```

### 4. `onResourceStart` / `onResourceStop`
Fired when any resource starts or stops:

```lua
AddEventHandler('onResourceStart', function(resourceName)
    if GetCurrentResourceName() == resourceName then
        print(string.format("Resource %s started successfully.", resourceName))
    end
end)
```

---

## Client-Side Built-in Events

### 1. `playerSpawned`
Fired by `spawnmanager` when the local player's character spawns:

```lua
AddEventHandler('playerSpawned', function(spawnInfo)
    print(string.format("Player spawned at: x=%.2f, y=%.2f, z=%.2f", spawnInfo.x, spawnInfo.y, spawnInfo.z))
end)
```

### 2. `gameEventTriggered` (C++ Engine Damage & Death Events)
Catches low-level GTA V engine events, such as entity damage and kills:

```lua
AddEventHandler('gameEventTriggered', function(name, args)
    if name == 'CEventNetworkEntityDamage' then
        local victim = args[1]
        local attacker = args[2]
        local isFatal = args[6] == 1
        local weaponHash = args[7]

        if isFatal and victim == PlayerPedId() then
            print(string.format("Local player died! Killed by entity: %s with weapon: 0x%X", attacker, weaponHash))
        end
    end
end)
```

### 3. `onClientResourceStart` / `onClientResourceStop`
Fired when a resource initializes or unloads on the client:

```lua
AddEventHandler('onClientResourceStart', function(resourceName)
    if GetCurrentResourceName() == resourceName then
        print("Client scripts initialized.")
    end
end)
```
