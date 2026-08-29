# Using Scaleform (Flash GFx UI) in FiveM

Scaleform GFx is GTA V's native vector interface framework. It powers in-game minimaps, instructional buttons, heists boards, and countdown timers with high performance.

## Lifecycle of a Scaleform Movie

1. **`RequestScaleformMovie(movieName)`**: Requests the GFx movie into GPU memory.
2. **`HasScaleformMovieLoaded(handle)`**: Waits until loaded.
3. **`BeginScaleformMovieMethod` / `EndScaleformMovieMethod`**: Calls ActionScript methods on the movie.
4. **`DrawScaleformMovieFullscreen` / `DrawScaleformMovie_3d`**: Renders on screen or in 3D space.
5. **`SetScaleformMovieAsNoLongerNeeded`**: Frees GPU memory when finished.

## Example: Instructional Buttons Bar (Bottom Right HUD)

```lua
local scaleform = nil

local function setupInstructionalButtons()
    local sf = RequestScaleformMovie("instructional_buttons")
    while not HasScaleformMovieLoaded(sf) do
        Wait(0)
    end

    BeginScaleformMovieMethod(sf, "CLEAR_ALL")
    EndScaleformMovieMethod()

    -- Button 1: [E] Interact (~INPUT_CONTEXT~)
    BeginScaleformMovieMethod(sf, "SET_DATA_SLOT")
    ScaleformMovieMethodAddParamInt(0)
    ScaleformMovieMethodAddParamPlayerNameString(GetControlInstructionalButton(2, 38, true))
    ScaleformMovieMethodAddParamTextureNameString("Interact")
    EndScaleformMovieMethod()

    -- Button 2: [BACKSPACE] Cancel (~INPUT_CELLPHONE_CANCEL~)
    BeginScaleformMovieMethod(sf, "SET_DATA_SLOT")
    ScaleformMovieMethodAddParamInt(1)
    ScaleformMovieMethodAddParamPlayerNameString(GetControlInstructionalButton(2, 177, true))
    ScaleformMovieMethodAddParamTextureNameString("Cancel")
    EndScaleformMovieMethod()

    BeginScaleformMovieMethod(sf, "DRAW_INSTRUCTIONAL_BUTTONS")
    EndScaleformMovieMethod()

    return sf
end

CreateThread(function()
    scaleform = setupInstructionalButtons()
    while scaleform do
        DrawScaleformMovieFullscreen(scaleform, 255, 255, 255, 255, 0)
        Wait(0)
    end
end)
```
