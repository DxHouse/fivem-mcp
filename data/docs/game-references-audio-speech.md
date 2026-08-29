# GTA V Audio, Radio Stations & Speeches Reference

Reference for GTA V radio station names, ambient speeches, ped voice names, and frontend soundsets.

## Radio Stations

| Radio Station Name | Genre / Format |
| :--- | :--- |
| `RADIO_01_CLASS_ROCK` | Los Santos Rock Radio |
| `RADIO_02_POP` | Non-Stop-Pop FM |
| `RADIO_03_HIPHOP_NEW` | Radio Los Santos |
| `RADIO_04_PUNK` | Channel X |
| `RADIO_05_TALK_01` | West Coast Talk Radio |
| `RADIO_06_COUNTRY` | Rebel Radio |
| `RADIO_11_HIPHOP_OLD` | West Coast Classics |
| `RADIO_16_SILVERLAKE` | Radio Mirror Park |
| `RADIO_OFF` | Turn Radio Off |

```lua
-- Set In-Vehicle Radio Station
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
SetVehRadioStation(vehicle, "RADIO_01_CLASS_ROCK")

-- Lock radio station or mute
SetUserRadioControlEnabled(false)
```

---

## Ambient Speeches & Ped Voices

```lua
-- Play ambient speech on a ped
-- Syntax: PlayPedAmbientSpeechNative(ped, speechName, speechParam)
local ped = PlayerPedId()
PlayPedAmbientSpeechNative(ped, "GENERIC_HI", "SPEECH_PARAMS_FORCE_NORMAL")

-- Common speech names:
-- "GENERIC_HI", "GENERIC_BYE", "GENERIC_CURSE_MED", "GENERIC_INSULT_MED", "GENERIC_SHOCK_MED"
-- "CHALLENGE_THREATEN", "SCREAM_PANIC", "WHATS_YOUR_PROBLEM"
```

---

## Frontend Soundsets

```lua
-- Play 2D Frontend sound
PlaySoundFrontend(-1, "NAV_UP_DOWN", "HUD_FRONTEND_DEFAULT_SOUNDSET", true)
PlaySoundFrontend(-1, "SELECT", "HUD_FRONTEND_DEFAULT_SOUNDSET", true)
PlaySoundFrontend(-1, "ERROR", "HUD_FRONTEND_DEFAULT_SOUNDSET", true)
PlaySoundFrontend(-1, "RACE_PLACED", "HUD_AWARDS", true)
```
