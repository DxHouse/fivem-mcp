# GTA V Weapon Hashes, Ped Models & Pickups Reference

Reference for GTA V weapon hashes grouped by category, common ped model names, and pickup hashes.

## Weapon Hashes by Category

### Melee
- `WEAPON_UNARMED` (`0xA2719263`)
- `WEAPON_KNIFE` (`0x99B507EA`)
- `WEAPON_BAT` (`0x958798F9`)
- `WEAPON_FLASHLIGHT` (`0x8BB05FD7`)

### Handguns
- `WEAPON_PISTOL` (`0x1B06D571`)
- `WEAPON_COMBATPISTOL` (`0x5EF9FEC4`)
- `WEAPON_APPISTOL` (`0x22D8FE39`)
- `WEAPON_PISTOL50` (`0x99AEEB3B`)
- `WEAPON_HEAVYPISTOL` (`0xD205520E`)

### Submachine Guns & Shotguns
- `WEAPON_MICROSMG` (`0x13532244`)
- `WEAPON_SMG` (`0x2BE67E01`)
- `WEAPON_PUMPSHOTGUN` (`0x1D073A89`)
- `WEAPON_SAWNOFFSHOTGUN` (`0x7846A318`)

### Assault Rifles & Snipers
- `WEAPON_ASSAULTRIFLE` (`0xBFEFFF6D`)
- `WEAPON_CARBINERIFLE` (`0x83BF0278`)
- `WEAPON_SPECIALCARBINE` (`0xC0A3098D`)
- `WEAPON_SNIPERRIFLE` (`0x05FC3C11`)
- `WEAPON_HEAVYSNIPER` (`0x0C472FE2`)

```lua
-- Give Weapon with Ammo to Player
local ped = PlayerPedId()
local weaponHash = `WEAPON_CARBINERIFLE`
GiveWeaponToPed(ped, weaponHash, 250, false, true)
SetCurrentPedWeapon(ped, weaponHash, true)
```

---

## Common Ped Models

- **Player Freemode:** `mp_m_freemode_01`, `mp_f_freemode_01`
- **Story Characters:** `player_zero` (Michael), `player_one` (Franklin), `player_two` (Trevor)
- **Police & Emergency:** `s_m_y_cop_01`, `s_m_y_sheriff_01`, `s_m_m_paramedic_01`, `s_m_y_fireman_01`
- **Civilians & Workers:** `a_m_y_beach_01`, `a_m_y_business_01`, `s_m_m_dockwork_01`, `u_m_m_bankman`

---

## Pickup Hashes

| Pickup Hash | Description |
| :--- | :--- |
| `PICKUP_HEALTH_STANDARD` (`0x8F707C18`) | First Aid Medkit |
| `PICKUP_ARMOUR_STANDARD` (`0x4BF86302`) | Body Armour Vest |
| `PICKUP_PARACHUTE` (`0x6773257D`) | Parachute |
| `PICKUP_MONEY_VARIABLE` (`0xFE185AB6`) | Cash bag / stack |
