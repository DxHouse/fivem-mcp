---
title: "OneSync & Routing Buckets Architecture"
description: "OneSync Infinity multiplayer architecture, server-authoritative entity creation, and virtual world routing."
keywords: ["onesync", "routing buckets", "dimensions", "createvehicleserversetter", "setplayerroutingbucket", "instances", "culling"]
---

# OneSync & Routing Buckets Architecture

OneSync is FiveM's multiplayer synchronization framework supporting server-authoritative world state, high player capacities (64-2048+ players), and spatial entity culling.

## 1. Quick Reference

| Function | APISet | Description |
| :--- | :--- | :--- |
| `CreateVehicleServerSetter(...)` | Server | Spawns authoritative networked vehicle |
| `SetPlayerRoutingBucket(src, bucketId)`| Server | Moves player into virtual dimension/bucket |
| `SetEntityRoutingBucket(entity, id)` | Server | Moves entity into virtual dimension/bucket |

## 2. Production Code Examples

```lua
-- SERVER SIDE: Spawning and isolating in Routing Bucket
local vehicle = CreateVehicleServerSetter(`adder`, "automobile", 215.0, -810.0, 30.5, 90.0)
local netId = NetworkGetNetworkIdFromEntity(vehicle)

-- Move into Apartment Bucket #105
SetPlayerRoutingBucket(source, 105)
SetEntityRoutingBucket(vehicle, 105)
```

## 3. Pitfalls & Best Practices

- **Never Spawn Networked Entities on Client in OneSync:** Client-spawned entities do not synchronize properly when no players are nearby.
