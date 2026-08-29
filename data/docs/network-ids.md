---
title: "Network and Local IDs in FiveM"
description: "Converting between local entity handles and synchronized OneSync Network IDs across client and server."
keywords: ["network id", "netid", "local handle", "entity handle", "onesync", "networkgetnetworkidfromentity", "networkgetentityfromnetworkid"]
---

# Network and Local IDs in FiveM

In FiveM, entity identification differs between client machines and the authoritative server.

## 1. Quick Reference

| Identifier Type | Scope | Example | Description |
| :--- | :--- | :--- | :--- |
| **Local Handle** | Client or Server Local | `12`, `485` | Memory handle local to a single GTA V machine |
| **Network ID (`netId`)**| Synchronized Globally | `1004`, `25601` | Global synchronized identifier managed by OneSync |

## 2. Production Code Examples

```lua
-- CLIENT SIDE: Convert Local Handle -> NetID
local localVehicle = GetVehiclePedIsIn(PlayerPedId(), false)
if DoesEntityExist(localVehicle) then
    local netId = NetworkGetNetworkIdFromEntity(localVehicle)
    TriggerServerEvent('garage:storeVehicle', netId)
end

-- SERVER SIDE: Convert NetID -> Server Entity Handle
RegisterNetEvent('garage:storeVehicle', function(netId)
    local serverVehicle = NetworkGetEntityFromNetworkId(netId)
    if DoesEntityExist(serverVehicle) then
        DeleteEntity(serverVehicle)
    end
end)
```

## 3. Pitfalls & Best Practices

- **Never Send Local Handles Over Network:** Local handles are meaningless across machines. Always convert to `netId` before triggering client/server events.
