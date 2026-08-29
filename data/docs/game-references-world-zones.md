# GTA V Map Zones, Profile Settings & Data Files Reference

Reference mapping 3-letter GTA V zone codes to full geographic names, profile settings, and resource data file schemas.

## GTA V Map Zones (3-Letter Codes)

| Zone Code | Full Name | Region |
| :--- | :--- | :--- |
| `AIRP` | Los Santos International Airport | Los Santos South |
| `ALAMO` | Alamo Sea | Blaine County |
| `ALTA` | Alta | Los Santos Central |
| `BANHAMC` | Banham Canyon | Los Santos West |
| `CHIL` | Vinewood Hills | Los Santos North |
| `DAVIS` | Davis | Los Santos South |
| `DELPE` | Del Perro | Los Santos West |
| `DOWNT` | Downtown | Los Santos Central |
| `HAWICK` | Hawick | Los Santos Central |
| `LEGION` | Legion Square | Los Santos Central |
| `MIRR` | Mirror Park | Los Santos East |
| `PALETO` | Paleto Bay | Blaine County |
| `PBLUFF` | Pacific Bluffs | Los Santos West |
| `SANDY` | Sandy Shores | Blaine County |
| `SKID` | Mission Row | Los Santos Central |
| `TEXTI` | Textile City | Los Santos Central |
| `VINE` | Vinewood | Los Santos North |

```lua
-- Get player's current zone code and translated name
local coords = GetEntityCoords(PlayerPedId())
local zoneCode = GetNameOfZone(coords.x, coords.y, coords.z)
local fullZoneName = GetLabelText(zoneCode)
print(string.format("Current Zone: %s (%s)", fullZoneName, zoneCode))
```

---

## Resource Manifest `data_file` Types

| Data File Directive | Target Asset |
| :--- | :--- |
| `HANDLING_FILE` | `handling.meta` (vehicle physics/handling) |
| `VEHICLE_METADATA_FILE` | `vehicles.meta` (model names, audio hash, flags) |
| `VEHICLE_LAYOUTS_FILE` | `vehiclelayouts.meta` (seat layout, doors) |
| `WEAPONINFO_FILE` | `weapons.meta` (damage, fire rates) |
| `PED_METADATA_FILE` | `peds.meta` (ped variations) |
| `DLC_ITYP_REQUEST` | `.ytyp` (archetype definitions for 3D map props) |
