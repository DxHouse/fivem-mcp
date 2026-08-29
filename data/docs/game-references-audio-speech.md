---
title: "GTA V Audio, Radio Stations & Speeches Reference"
description: "Reference for GTA V radio station names, ambient speeches, ped voice names, and frontend soundsets."
keywords: ["audio", "radio", "radio stations", "speech", "soundsets", "playsoundfrontend", "voices", "sounds"]
---

# GTA V Audio, Radio Stations & Speeches Reference

Reference for GTA V radio station names, ambient speeches, ped voice names, and frontend soundsets.

## 1. Quick Reference

| Radio Station | Genre / Name | Ambient Speech Name | Soundset Name |
| :--- | :--- | :--- | :--- |
| `RADIO_01_CLASS_ROCK` | Los Santos Rock Radio | `GENERIC_HI` | `HUD_FRONTEND_DEFAULT_SOUNDSET` |
| `RADIO_02_POP` | Non-Stop-Pop FM | `GENERIC_BYE` | `HUD_AWARDS` |
| `RADIO_03_HIPHOP_NEW` | Radio Los Santos | `GENERIC_CURSE_MED` | `NAV_UP_DOWN` |
| `RADIO_OFF` | Turn Radio Off | `SCREAM_PANIC` | `SELECT` |

## 2. Production Code Examples

```lua
-- Play Frontend 2D Sound Effect
PlaySoundFrontend(-1, "SELECT", "HUD_FRONTEND_DEFAULT_SOUNDSET", true)

-- Trigger Ped Ambient Speech
PlayPedAmbientSpeechNative(PlayerPedId(), "GENERIC_HI", "SPEECH_PARAMS_FORCE_NORMAL")
```

## 3. Pitfalls & Best Practices

- **Soundset Parameter:** The 3rd parameter in `PlaySoundFrontend` must be a valid GTA V soundset name, otherwise the sound fails silently.
