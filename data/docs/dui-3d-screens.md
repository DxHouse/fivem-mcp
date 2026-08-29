# Direct-Rendered UI (DUI 3D In-Game Screens)

DUI (Direct-Rendered UI) allows developers to render web pages directly onto in-game 3D world models, televisions, cinema screens, billboards, and computer terminals.

## How DUI Works

1. **Create the DUI Browser Object (`CreateDui`)**: Spawns an offscreen Chromium web renderer.
2. **Fetch Texture Handle (`GetDuiHandle`)**: Retrieves the GPU texture handle from the web renderer.
3. **Link to Render Target Texture (`CreateRuntimeTextureFromDuiHandle`)**: Maps the DUI texture onto a named game texture dictionary (`txd`).
4. **Draw onto In-Game Prop**: Uses `RegisterNamedRendertarget` to display the texture on a specific model mesh.

## Complete DUI Setup Example

```lua
local duiObject = nil
local txd = nil
local textureName = "dui_screen_tex"
local txdName = "dui_screen_txd"
local targetModel = `prop_tv_flat_01`
local renderTargetName = "tvscreen"

CreateThread(function()
    -- 1. Create DUI Browser (Width: 1280, Height: 720)
    duiObject = CreateDui('https://www.youtube.com', 1280, 720)
    local duiHandle = GetDuiHandle(duiObject)

    -- 2. Create Runtime Texture Dictionary
    txd = CreateRuntimeTxd(txdName)
    CreateRuntimeTextureFromDuiHandle(txd, textureName, duiHandle)

    -- 3. Link Render Target to Prop
    RegisterNamedRendertarget(renderTargetName, false)
    LinkNamedRendertarget(targetModel)
    local handle = GetNamedRendertargetRenderId(renderTargetName)

    -- 4. Drawing Loop
    while duiObject do
        SetTextRenderId(handle)
        Set_2dLayer(4)
        SetScriptGfxDrawBehindPausemenu(true)
        DrawRect(0.5, 0.5, 1.0, 1.0, 0, 0, 0, 255)
        DrawSprite(txdName, textureName, 0.5, 0.5, 1.0, 1.0, 0.0, 255, 255, 255, 255)
        SetTextRenderId(GetDefaultScriptRendertargetRenderId())
        Wait(0)
    end
end)

-- Cleanup on Resource Stop
AddEventHandler('onResourceStop', function(res)
    if res == GetCurrentResourceName() and duiObject then
        DestroyDui(duiObject)
        duiObject = nil
    end
end)
```

## DUI Best Practices

- **Always Clean Up (`DestroyDui`)**: Failing to destroy DUI instances when closing or stopping resources causes GPU memory leaks.
- **Limit Resolution**: Use 1280x720 or 1920x1080. Higher resolutions increase VRAM usage significantly.
