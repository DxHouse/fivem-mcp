# FiveM Native Fuel Consumption Subsystem

FiveM provides a built-in native vehicle fuel simulation subsystem, removing the need for heavy custom tick-loop math.

## Enabling and Managing Fuel State

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)

-- 1. Enable native fuel consumption for a vehicle
SetFuelConsumptionState(vehicle, true)

-- 2. Read and write fuel level (0.0 to 100.0)
local currentFuel = GetVehicleFuelLevel(vehicle)
SetVehicleFuelLevel(vehicle, 65.0)

-- 3. Adjust consumption rate multiplier (1.0 = normal, 2.0 = double consumption)
SetFuelConsumptionRateMultiplier(vehicle, 1.25)
```

## Integrating with Vehicle Handling

Native fuel calculation accounts for engine RPM, throttle input, and vehicle class automatically.

```lua
-- Example: Gas Station Refuel Loop
local function refuelVehicle(vehicle)
    local fuel = GetVehicleFuelLevel(vehicle)
    while fuel < 100.0 do
        Wait(200)
        fuel = math.min(100.0, fuel + 2.0)
        SetVehicleFuelLevel(vehicle, fuel)
    end
    print("Refuel complete!")
end
```
