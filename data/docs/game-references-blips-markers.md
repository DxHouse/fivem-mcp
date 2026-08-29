---
title: "Blips, Markers & Checkpoints Reference"
description: "Reference for GTA V minimap blip sprite IDs, colors, 3D world markers (0-43), and checkpoints."
keywords: ["blips", "markers", "checkpoints", "addblipforcoord", "drawmarker", "sprites", "blip colors"]
---

# Blips, Markers & Checkpoints Reference

Reference for GTA V minimap blip sprite IDs, blip colors, 3D world markers (0-43), and checkpoints.

## 1. Quick Reference

| Blip Sprite ID | Description | Marker Type | Name | Shape |
| :--- | :--- | :--- | :--- | :--- |
| `1` | Destination Circle | `1` | Cylinder | Flat vertical cylinder on ground |
| `52` | Police Station | `2` | Chevron | Bouncing downward chevron |
| `110` | Gun Shop | `21` | Horizontal Ring | Ring parallel to ground |
| `153` | Hospital | `27` | Split Arrow | Ground directional circle |
| `318` | Gas Station | `36` | Car Symbol | Rotating 3D vehicle icon |

## 2. Production Code Examples

```lua
-- Create a Minimap Blip
local blip = AddBlipForCoord(100.0, -200.0, 30.0)
SetBlipSprite(blip, 318) -- Gas Station
SetBlipColour(blip, 5)   -- Yellow
SetBlipScale(blip, 0.8)
SetBlipAsShortRange(blip, true)

-- Draw a 3D Glowing Cylinder Marker on ground
DrawMarker(1, 100.0, -200.0, 29.0, 0,0,0, 0,0,0, 1.5, 1.5, 0.75, 255, 50, 50, 200, false, false, 2, false, nil, nil, false)
```

## 3. Pitfalls & Best Practices

- **Offset Z for Ground Cylinders:** Subtract ~1.0 from entity Z coords so cylinder markers rest flush with the terrain.
