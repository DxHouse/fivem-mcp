---
title: "HUD Colors, Text Formatting & Gamer Tags Reference"
description: "Reference for GTA V text formatting color tokens, HUD color IDs, and overhead player Gamer Tags."
keywords: ["hud colors", "text formatting", "gamer tags", "colors", "~r~", "~g~", "~h~", "hud", "notifications"]
---

# HUD Colors, Text Formatting & Gamer Tags Reference

Reference for GTA V text formatting color tokens, HUD color IDs, and overhead player Gamer Tags.

## 1. Quick Reference & Text Tokens

| Token | Effect | Example |
| :--- | :--- | :--- |
| `~r~` | Red text | `~r~Critical Danger` |
| `~g~` | Green text | `~g~Transaction Approved` |
| `~b~` | Blue text | `~b~GPS Routing` |
| `~y~` | Yellow text | `~y~Warning Alert` |
| `~h~` | Bold text | `~h~Bold Header~h~` |
| `~s~` / `~w~` | Reset to White | `~s~Regular Text` |
| `~INPUT_CONTEXT~` | [E] Button Icon | `Press ~INPUT_CONTEXT~ to open` |

## 2. Production Code Examples

```lua
-- In-Game Formatted Notification
BeginTextCommandThefeedPost("STRING")
AddTextComponentSubstringPlayerName("~g~[SUCCESS]~s~ Payment of ~y~$500~s~ received.")
EndTextCommandThefeedPostTicker(false, true)
```

## 3. Pitfalls & Best Practices

- **Always Close Formatting Tokens:** End color spans with `~s~` to prevent formatting from bleeding into the rest of the text.
