---
title: "GTA V Map Zones, Profile Settings & Data Files Reference"
description: "Reference mapping 3-letter GTA V zone codes to full geographic names, profile settings, and data file schemas."
keywords: ["zones", "map zones", "data files", "handling_file", "vehicle_metadata_file", "getnameofzone", "neighborhoods"]
---

# GTA V Map Zones, Profile Settings & Data Files Reference

Reference mapping 3-letter GTA V zone codes to full geographic names, profile settings, and resource data file schemas.

## 1. Quick Reference & Zone Mapping

| Zone Code | Full Name | Region |
| :--- | :--- | :--- |
| `AIRP` | Los Santos International Airport | Los Santos South |
| `DOWNT` | Downtown | Los Santos Central |
| `LEGION` | Legion Square | Los Santos Central |
| `PALETO` | Paleto Bay | Blaine County |
| `SANDY` | Sandy Shores | Blaine County |
| `VINE` | Vinewood | Los Santos North |

## 2. Production Code Examples

```lua
local coords = GetEntityCoords(PlayerPedId())
local zoneCode = GetNameOfZone(coords.x, coords.y, coords.z)
local fullZoneName = GetLabelText(zoneCode)
print(string.format("Current Location: %s (%s)", fullZoneName, zoneCode))
```

## 3. Pitfalls & Best Practices

- **Translating Zone Codes:** `GetNameOfZone` returns a 3-4 character uppercase code (e.g. `AIRP`). Always wrap with `GetLabelText(zoneCode)` to get the localized text string.
