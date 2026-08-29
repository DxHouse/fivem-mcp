# GTA V Vehicle Models, Colors & Flags Reference

Reference for GTA V vehicle models grouped by class, vehicle paint colors (0-159), and vehicle handling flags.

## Popular Vehicle Models by Class

### Super / Sports
- `adder`, `zentorno`, `t20`, `nero`, `turismor`, `prototipo`, `krieger`, `emerus`, `pariah`, `italigto`

### Sedans / Coupes / Muscle
- `kuruma`, `sultan`, `tailgater`, `schafter2`, `dominator`, `gauntlet`, `elegy2`, `buffalo`

### Emergency & Service
- `police`, `police2`, `police3`, `police4`, `policeb`, `sheriff`, `sheriff2`, `ambulance`, `firetruk`, `taxi`

### SUVs / Off-Road / Trucks
- `baller`, `granger`, `dubsta`, `sandking`, `bifta`, `kamacho`, `mule`, `hauler`, `phantom`

---

## Vehicle Paint Color Indices (0 - 159)

| Color ID | Name | Category |
| :--- | :--- | :--- |
| `0` | Metallic Black | Classic / Metallic |
| `27` | Metallic Red | Classic / Metallic |
| `64` | Metallic Blue | Classic / Metallic |
| `88` | Metallic Yellow | Classic / Metallic |
| `111` | Metallic Classic White | Classic / Metallic |
| `12` | Matte Black | Matte |
| `39` | Matte Red | Matte |
| `83` | Matte Blue | Matte |
| `117` | Brushed Steel | Metals |
| `120` | Chrome | Metals |
| `158` | Pure Gold | Metals |

```lua
-- Apply Primary and Secondary Paint Colors
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
SetVehicleColours(vehicle, 120, 0) -- Chrome primary, Metallic Black secondary
SetVehicleExtraColours(vehicle, 111, 0) -- Pearlescent white, Black wheels
```

---

## Vehicle Flags & Handling Modifiers

```lua
-- Common Vehicle Flags & Toggles
SetVehicleEngineOn(vehicle, true, true, false)
SetVehicleUndriveable(vehicle, false)
SetVehicleDoorsLocked(vehicle, 2) -- 2 = Locked, 1 = Unlocked, 4 = Locked for non-driver
SetVehicleTyreBurst(vehicle, 0, true, 1000.0) -- Puncture front-left tyre
```
