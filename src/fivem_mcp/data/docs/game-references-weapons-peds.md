---
title: "GTA V Weapon Hashes, Ped Models & Pickups Reference"
description: "Reference for GTA V weapon hashes grouped by category, common ped model names, and pickup hashes."
keywords: ["weapons", "peds", "pickups", "weapon hashes", "ped models", "guns", "loadout", "giveweapontoped"]
---

# GTA V Weapon Hashes, Ped Models & Pickups Reference

Reference for GTA V weapon hashes grouped by category, common ped model names, and pickup hashes.

## 1. Quick Reference

- **Handguns:** `WEAPON_PISTOL` (`0x1B06D571`), `WEAPON_COMBATPISTOL` (`0x5EF9FEC4`), `WEAPON_HEAVYPISTOL` (`0xD205520E`)
- **Rifles & SMGs:** `WEAPON_SMG` (`0x2BE67E01`), `WEAPON_ASSAULTRIFLE` (`0xBFEFFF6D`), `WEAPON_CARBINERIFLE` (`0x83BF0278`)
- **Ped Models:** `mp_m_freemode_01`, `mp_f_freemode_01`, `s_m_y_cop_01`, `s_m_m_paramedic_01`
- **Pickups:** `PICKUP_HEALTH_STANDARD` (`0x8F707C18`), `PICKUP_ARMOUR_STANDARD` (`0x4BF86302`)

## 2. Production Code Examples

```lua
local ped = PlayerPedId()
local weaponHash = `WEAPON_CARBINERIFLE`
GiveWeaponToPed(ped, weaponHash, 250, false, true)
SetCurrentPedWeapon(ped, weaponHash, true)
```

## 3. Pitfalls & Best Practices

- **Use Backtick Hashes in Lua 5.4:** In Lua 5.4, `` `WEAPON_PISTOL` `` is automatically computed as an integer hash at compile time with zero runtime string hashing cost.
