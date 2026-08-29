# Blips, Markers & Checkpoints Reference

Reference for GTA V minimap blip sprite IDs, blip colors, 3D world markers (0-43), and checkpoints.

## Blip Sprites & Colors

### Common Blip Sprite IDs
| Sprite ID | Description |
| :--- | :--- |
| `1` | Standard Destination Circle / Square |
| `52` | Police Station |
| `60` | Police Officer Shield |
| `67` | Helicopter |
| `110` | Gun / Ammu-Nation |
| `153` | Hospital / Health Cross |
| `225` | Car / Garage |
| `318` | Gas Station / Fuel |
| `500` | Repair Wrench |
| `523` | Warehouse / Storage |

### Common Blip Color IDs
| Color ID | Color Name |
| :--- | :--- |
| `0` | White |
| `1` | Red |
| `2` | Green |
| `3` | Blue |
| `5` | Yellow |
| `6` | Orange |
| `38` | Dark Blue |
| `47` | Orange-Red |
| `49` | Light Green |

```lua
-- Create and configure a Blip
local blip = AddBlipForCoord(coords.x, coords.y, coords.z)
SetBlipSprite(blip, 318) -- Gas Station
SetBlipColour(blip, 5)   -- Yellow
SetBlipScale(blip, 0.8)
SetBlipAsShortRange(blip, true)
BeginTextCommandSetBlipName("STRING")
AddTextComponentString("Gas Station")
EndTextCommandSetBlipName(blip)
```

---

## 3D World Markers (Types 0 - 43)

| Marker Type | Name | Visual Shape |
| :--- | :--- | :--- |
| `0` | Cone | Upside-down triangle cone |
| `1` | Cylinder | Flat vertical cylinder on ground |
| `2` | Chevron | Animated bouncing chevron pointing down |
| `20` | Chevron Up | Animated chevron pointing up |
| `21` | Horizontal Ring | Ring parallel to ground |
| `27` | Horizontal Split Arrow | Ground directional circle |
| `36` | Car / Garage Icon | Rotating 3D vehicle symbol |

```lua
-- Draw a red glowing cylinder on ground (runs inside Wait(0) thread)
DrawMarker(
    1, -- Cylinder
    coords.x, coords.y, coords.z - 1.0, -- position
    0.0, 0.0, 0.0, -- dir
    0.0, 0.0, 0.0, -- rot
    1.5, 1.5, 0.75, -- scale (x, y, z)
    255, 50, 50, 200, -- color (r, g, b, a)
    false, false, 2, false, nil, nil, false
)
```
