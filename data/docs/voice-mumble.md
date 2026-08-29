# FiveM Voice & Mumble Integration

FiveM includes a high-performance built-in Mumble voice implementation with 3D positional audio, proximity grids, channels, and submix effects.

## Proximity Voice Configuration

```lua
-- Set voice proximity radius (in meters)
local proximityDistances = {
    whisper = 1.5,
    normal = 5.0,
    shout = 15.0
}

MumbleSetTalkerProximity(proximityDistances.normal)

-- Enable 3D voice positioning
MumbleSetAudioInputDistance(5.0)
MumbleSetAudioOutputDistance(5.0)
```

## Radio Channels & Call Groups

```lua
-- Join a radio channel (e.g. Channel 1 for Police)
local radioChannel = 1
MumbleAddVoiceTargetChannel(1, radioChannel)
MumbleSetVoiceChannel(radioChannel)

-- Leave radio channel
MumbleClearVoiceTargetChannels(1)
```

## Submix Audio Effects (Radio / Megaphone Distortion)

FiveM allows applying DSP audio submixes (equalizer, distortion, high-pass filter) to simulate police radio or telephone sounds:

```lua
-- 1. Create Submix
local radioSubmix = CreateAudioSubmix('Radio')

-- 2. Apply Bandpass Filter (300Hz - 3400Hz telephone/walkie-talkie spectrum)
SetAudioSubmixEffectRadioFx(radioSubmix, 0)
SetAudioSubmixEffectParamInt(radioSubmix, 0, `default`, 1)
AddAudioSubmixOutput(radioSubmix, 0)

-- 3. Route specific player audio through the submix
MumbleSetSubmixForServerId(targetServerId, radioSubmix)
```
