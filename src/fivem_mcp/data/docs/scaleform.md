---
title: "Using Scaleform (Flash GFx UI) in FiveM"
description: "Rendering high-performance Scaleform Flash movies, instructional buttons, and HUD elements."
keywords: ["scaleform", "gfx", "instructional buttons", "flash", "requestscaleformmovie", "minimap", "hud"]
---

# Using Scaleform (Flash GFx UI) in FiveM

Scaleform GFx is GTA V's native vector interface framework powering instructional button bars, countdown timers, and minimap HUDs.

## 1. Quick Reference

| Function | Description |
| :--- | :--- |
| `RequestScaleformMovie(name)` | Loads GFx movie into GPU memory |
| `HasScaleformMovieLoaded(handle)` | Checks if movie is ready |
| `DrawScaleformMovieFullscreen(...)` | Renders movie on screen |
| `SetScaleformMovieAsNoLongerNeeded(...)` | Frees GPU movie memory |

## 2. Production Code Examples

```lua
local sf = RequestScaleformMovie("instructional_buttons")
while not HasScaleformMovieLoaded(sf) do Wait(0) end

BeginScaleformMovieMethod(sf, "CLEAR_ALL")
EndScaleformMovieMethod()

BeginScaleformMovieMethod(sf, "SET_DATA_SLOT")
ScaleformMovieMethodAddParamInt(0)
ScaleformMovieMethodAddParamPlayerNameString(GetControlInstructionalButton(2, 38, true))
ScaleformMovieMethodAddParamTextureNameString("Interact")
EndScaleformMovieMethod()

BeginScaleformMovieMethod(sf, "DRAW_INSTRUCTIONAL_BUTTONS")
EndScaleformMovieMethod()
```

## 3. Pitfalls & Best Practices

- **Always Free Scaleform Handles:** Call `SetScaleformMovieAsNoLongerNeeded` when closing UI elements.
