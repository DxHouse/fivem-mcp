---
title: "GTA V Vehicle Models, Colors & Flags Reference"
description: "Reference for GTA V vehicle models grouped by class, vehicle paint colors (0-159), and vehicle handling flags."
keywords: ["vehicles", "cars", "vehicle models", "vehicle colors", "paint", "handling flags", "supercars", "spawn vehicle"]
---

# GTA V Vehicle Models, Colors & Flags Reference

Reference for GTA V vehicle models grouped by class, vehicle paint colors (0-159), and vehicle handling flags.

## 1. Quick Reference & Models

- **Super / Sports:** `adder`, `zentorno`, `t20`, `nero`, `turismor`, `prototipo`, `krieger`, `emerus`, `pariah`
- **Sedans & Muscle:** `kuruma`, `sultan`, `tailgater`, `dominator`, `gauntlet`, `elegy2`, `buffalo`
- **Emergency:** `police`, `police2`, `police3`, `police4`, `sheriff`, `ambulance`, `firetruk`
- **Paint Types:** Classic/Metallic (`0` Black, `27` Red, `64` Blue), Matte (`12` Black, `39` Red), Metals (`120` Chrome, `158` Gold)

## 2. Production Code Examples

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
SetVehicleColours(vehicle, 120, 0) -- Chrome primary, Black secondary
SetVehicleDoorsLocked(vehicle, 2) -- 2 = Locked
```

## 3. Pitfalls & Best Practices

- **Validate Model Hashes:** Always check `IsModelInCdimage(model)` and `IsModelAVehicle(model)` before loading vehicle model assets.
