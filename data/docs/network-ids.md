# Network and Local IDs in FiveM

In FiveM, entity identification differs between client machines and the server.

## Local Handle vs Network ID

- **Local Entity Handle (`entity`)**: An integer assigned locally by GTA V's game engine on a specific machine. Local handles are NOT valid across machines (Ped #12 on Client A might be Ped #45 on Client B).
- **Network ID (`netId`)**: A synchronized integer assigned by FiveM/OneSync representing the entity globally across all clients and the server.

## Converting Between Handles and Network IDs

```lua
-- ===================================
-- CLIENT SIDE: Handle -> Network ID
-- ===================================
local localVehicle = GetVehiclePedIsIn(PlayerPedId(), false)
if DoesEntityExist(localVehicle) then
    local netId = NetworkGetNetworkIdFromEntity(localVehicle)
    
    -- Send netId to server
    TriggerServerEvent('garage:storeVehicle', netId)
end

-- ===================================
-- SERVER SIDE: Network ID -> Handle
-- ===================================
RegisterNetEvent('garage:storeVehicle', function(netId)
    local serverVehicle = NetworkGetEntityFromNetworkId(netId)
    if DoesEntityExist(serverVehicle) then
        DeleteEntity(serverVehicle)
    end
end)
```

## OneSync & Entity Routing

1. **Server-Side Entity Spawning:**
   - Always spawn persistent networked vehicles and peds on the **server** using `CreateVehicleServerSetter` or `CreatePed`.
2. **Entity Existence Checks:**
   - Always check `DoesEntityExist(entity)` before reading coords, state, or deleting entities.
3. **Network Owner Migration:**
   - Network ownership dynamically migrates to whichever client is closest to the entity.
   - Use `NetworkGetEntityOwner(entity)` to see which client currently controls entity physics.
