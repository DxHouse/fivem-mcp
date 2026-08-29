# FiveM Networking & Events Guide

FiveM uses an asynchronous, message-based event system to communicate between the Client and Server.

## Core Event APIs

### 1. Registering & Handling Events

```lua
-- Register a network-accessible event handler
RegisterNetEvent('myResource:customEvent', function(data)
    -- In server context: 'source' variable automatically contains the player ID
    local src = source
    print(string.format("Received event from player %s with data: %s", src, json.encode(data)))
end)
```

### 2. Triggering Events Across the Network

```lua
-- CLIENT -> SERVER:
TriggerServerEvent('myResource:serverAction', { itemId = 123, count = 1 })

-- SERVER -> SPECIFIC CLIENT:
local targetPlayerId = 1
TriggerClientEvent('myResource:clientNotify', targetPlayerId, 'You received an item!')

-- SERVER -> ALL CLIENTS (Broadcast):
TriggerClientEvent('myResource:globalAnnouncement', -1, 'Server restarting in 5 minutes!')
```

### 3. Local (Same-Side) Events

```lua
-- Trigger an event on the SAME environment (client->client or server->server)
TriggerEvent('myResource:localEvent', payload)
```

## Security Best Practices

1. **NEVER Trust Client Payloads:**
   - Never accept money amounts, item counts, or admin status directly from client event arguments.
   - Always validate player permissions and inventories on the **server side**.
2. **Always Use `source` on Server:**
   - Capture `local src = source` at the start of the event handler. Do not rely on client-passed player IDs.
3. **Rate Limiting & Anti-Spam:**
   - Add timestamp cooldowns on critical network events to prevent trigger execution exploitation.

## Latent Network Events (Large Payloads)

For transferring large payloads (e.g. data > 64 KB) without choking the network frame:

```lua
-- Server: Send data throttled at 50,000 bytes/sec
TriggerLatentClientEvent('myResource:receiveLargeMap', targetPlayerId, 50000, largeDataPayload)
```
