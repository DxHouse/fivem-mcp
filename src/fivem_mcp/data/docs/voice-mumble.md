---
title: "FiveM Voice & Mumble Integration"
description: "Built-in Mumble 3D spatial voice, proximity grids, radio channels, and DSP submix audio routing."
keywords: ["voice", "mumble", "proximity", "radio", "submix", "3d audio", "radio filter", "mumblesetvoicetargetchannel"]
---

# FiveM Voice & Mumble Integration

FiveM includes a high-performance built-in Mumble voice implementation with 3D positional audio and DSP submix filters.

## 1. Quick Reference

| Function | Description |
| :--- | :--- |
| `MumbleSetTalkerProximity(distance)` | Sets local voice transmission range in meters |
| `MumbleSetVoiceChannel(channel)` | Joins a specific radio/voice channel |
| `CreateAudioSubmix(name)` | Creates an audio DSP pipeline |

## 2. Production Code Examples

```lua
-- Radio Submix with Bandpass Effect (Walkie-Talkie Sound)
local radioSubmix = CreateAudioSubmix('Radio')
SetAudioSubmixEffectRadioFx(radioSubmix, 0)
SetAudioSubmixEffectParamInt(radioSubmix, 0, `default`, 1)
AddAudioSubmixOutput(radioSubmix, 0)
MumbleSetSubmixForServerId(targetServerId, radioSubmix)
```

## 3. Pitfalls & Best Practices

- **Avoid Global Channels for Proximity:** Keep spatial voice on Grid channels and use dedicated channels strictly for Radios/Phone calls.
