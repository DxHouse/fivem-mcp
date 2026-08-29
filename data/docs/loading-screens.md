# Custom Loading Screens Guide

Loading screens in FiveM are specialized NUI web pages displayed while players connect, download assets, and initialize game collision.

## `fxmanifest.lua` Declarations

```lua
fx_version 'cerulean'
game 'gta5'

-- 1. Declare the main loading screen HTML file
loadingscreen 'web/index.html'

-- 2. Keep the loading screen active until scripts explicitly shut it down
loadingscreen_manual_shutdown 'yes'

-- 3. (Optional) Enable cursor during loading
loadingscreen_cursor 'yes'

files {
    'web/index.html',
    'web/assets/*.*',
    'web/music.mp3'
}
```

## Listening to Loading Events (JavaScript)

FiveM sends progress events to the loading screen window:

```javascript
window.addEventListener('message', (event) => {
    const data = event.data;
    
    if (data.eventName === 'loadProgress') {
        const fraction = data.loadFraction; // 0.0 to 1.0
        document.getElementById('progress-bar').style.width = (fraction * 100) + '%';
    }
    
    if (data.eventName === 'onDataFileEntry') {
        document.getElementById('status').innerText = `Loading: ${data.name}`;
    }
});
```

## Manual Shutdown from Client Lua

When using `loadingscreen_manual_shutdown 'yes'`, the loading screen stays visible until the client script is fully initialized:

```lua
CreateThread(function()
    -- Wait until player character is spawned and collision is loaded
    while not NetworkIsPlayerActive(PlayerId()) do
        Wait(500)
    end

    -- Fade in player screen
    DoScreenFadeOut(0)
    
    -- Shutdown the loading screen NUI
    ShutdownLoadingScreenNui()
    
    Wait(1000)
    DoScreenFadeIn(1000)
end)
```
