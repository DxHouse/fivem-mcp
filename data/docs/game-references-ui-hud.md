# HUD Colors, Text Formatting & Gamer Tags Reference

Reference for GTA V text formatting color tokens, HUD color IDs, and overhead player Gamer Tags.

## In-Game Text Formatting Tokens

Tokens can be embedded directly inside game strings (notifications, subtitles, help text):

| Token | Formatting / Effect | Example Output |
| :--- | :--- | :--- |
| `~r~` | Red text | `~r~Warning:` |
| `~g~` | Green text | `~g~Success!` |
| `~b~` | Blue text | `~b~Info:` |
| `~y~` | Yellow text | `~y~Caution` |
| `~o~` | Orange text | `~o~Alert` |
| `~p~` | Purple text | `~p~Special` |
| `~w~` | Reset to White | `~w~Regular text` |
| `~h~` | Bold text | `~h~Bold Title~h~` |
| `~s~` | Default white text | `~s~Standard` |
| `~n~` | New line | `Line 1~n~Line 2` |
| `~INPUT_CONTEXT~` | Controller/Key icon for [E] | `Press ~INPUT_CONTEXT~ to open` |

```lua
-- Drawing an in-game notification with formatted text
BeginTextCommandThefeedPost("STRING")
AddTextComponentSubstringPlayerName("~g~[SUCCESS]~s~ Payment of ~y~$500~s~ received.")
EndTextCommandThefeedPostTicker(false, true)
```

---

## HUD Colors & RGB Palette

| HUD Color Index | Name | HEX / RGB Equivalent |
| :--- | :--- | :--- |
| `HUD_COLOUR_PURE_WHITE` (0) | Pure White | `#FFFFFF` |
| `HUD_COLOUR_WHITE` (1) | Standard White | `#F0F0F0` |
| `HUD_COLOUR_BLACK` (2) | Black | `#000000` |
| `HUD_COLOUR_GREY` (3) | Grey | `#969696` |
| `HUD_COLOUR_RED` (6) | System Red | `#E11E1E` |
| `HUD_COLOUR_GREEN` (8) | System Green | `#72BE50` |
| `HUD_COLOUR_BLUE` (9) | System Blue | `#4E85C8` |
| `HUD_COLOUR_YELLOW` (10) | System Yellow | `#D8B400` |

---

## Gamer Tags (Overhead Player Names & Health Bars)

```lua
-- Create and configure a GamerTag for target player ped
local tag = CreateMpGamerTag(targetPed, "PlayerName", false, false, "", 0)
SetMpGamerTagVisibility(tag, 0, true) -- 0: GAMER_NAME
SetMpGamerTagVisibility(tag, 2, true) -- 2: HEALTH_ARMOUR
SetMpGamerTagColour(tag, 0, 0)        -- White text
```
