# OneSync & Routing Buckets Architecture

OneSync is FiveM's multiplayer synchronization framework supporting server-authoritative world state, high player capacities (64-2048+ players), and spatial entity culling.

## Server-Authoritative Entity Creation (`CreateVehicleServerSetter`)

Under OneSync Infinity, vehicles and peds spawned from clients when no players are nearby will fail to materialize. Always create persistent networked entities on the **Server**:

```lua
-- SERVER SIDE:
local model = `adder`
local type = "automobile" -- "automobile", "bike", "boat", "heli", "plane", "trailer"
local coords = vector3(215.0, -810.0, 30.5)
local heading = 90.0

-- Create vehicle via OneSync server setter
local vehicle = CreateVehicleServerSetter(model, type, coords.x, coords.y, coords.z, heading)
local netId = NetworkGetNetworkIdFromEntity(vehicle)

-- Wait for entity initialization
while not DoesEntityExist(vehicle) do
    Wait(0)
end

print("Server vehicle spawned with Network ID:", netId)
```

## Routing Buckets (Virtual Worlds & Dimensions)

Routing buckets isolate players and entities into distinct virtual dimensions. Entities and players in Bucket 1 cannot see, hear, or collide with players in Bucket 2:

```lua
-- ===================================
-- SERVER SIDE: Routing Buckets
-- ===================================

local apartmentBucketId = 105

-- 1. Route player into apartment instance
SetPlayerRoutingBucket(source, apartmentBucketId)

-- 2. Route an entity (e.g. vehicle) into a specific bucket
SetEntityRoutingBucket(vehicle, apartmentBucketId)

-- 3. Return player to main world (Bucket 0 is default world)
SetPlayerRoutingBucket(source, 0)

-- 4. Check player's current bucket
local currentBucket = GetPlayerRoutingBucket(source)
print("Player is in bucket:", currentBucket)
```

## Population & Culling Configuration

```lua
-- Lock routing bucket population (disable ambient traffic/pedestrians inside apartments)
SetRoutingBucketPopulationEnabled(apartmentBucketId, false)

-- Disable auto-culling of vehicles parked in apartment garages
SetEntityDistanceCullingRadius(vehicle, 0.0)
```
