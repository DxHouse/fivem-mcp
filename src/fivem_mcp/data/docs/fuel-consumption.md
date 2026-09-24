---
title: "FiveM Native Fuel Consumption Subsystem"
description: "Managing vehicle fuel levels and consumption rates with FiveM native engine multipliers."
keywords: ["fuel", "gas", "gas station", "setvehiclefuellevel", "getvehiclefuellevel", "setfuelconsumptionstatemultiplier"]
---

# FiveM Native Fuel Consumption Subsystem

FiveM provides a built-in native vehicle fuel simulation subsystem that eliminates heavy custom frame-tick calculation loops.

## 1. Quick Reference

| Function | Description |
| :--- | :--- |
| `SetFuelConsumptionState(vehicle, state)` | Enables or disables native fuel consumption |
| `GetVehicleFuelLevel(vehicle)` | Reads current fuel level (0.0 - 100.0) |
| `SetVehicleFuelLevel(vehicle, level)` | Sets current fuel level |
| `SetFuelConsumptionRateMultiplier(vehicle, mult)` | Multiplies fuel burn rate (1.0 = normal) |

## 2. Production Code Examples

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
SetFuelConsumptionState(vehicle, true)
SetVehicleFuelLevel(vehicle, 80.0)
SetFuelConsumptionRateMultiplier(vehicle, 1.2)
```

## 3. Pitfalls & Best Practices

- **Zero CPU Overhead:** Use native fuel functions instead of running custom `while true do Wait(1000)` fuel decay threads.
