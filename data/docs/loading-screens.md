---
title: "Custom Loading Screens Guide"
description: "Creating custom loading screens, listening to progress events, and manual shutdown controls."
keywords: ["loadingscreen", "loading screen", "loadingscreen_manual_shutdown", "shutdownloadingscreennui", "nui loading"]
---

# Custom Loading Screens Guide

Loading screens in FiveM are specialized NUI web pages displayed while players connect and download assets.

## 1. Quick Reference & Manifest Directives

```lua
loadingscreen 'web/index.html'
loadingscreen_manual_shutdown 'yes'
loadingscreen_cursor 'yes'
```

## 2. Production Code Examples

```lua
CreateThread(function()
    while not NetworkIsPlayerActive(PlayerId()) do
        Wait(500)
    end
    ShutdownLoadingScreenNui()
end)
```

## 3. Pitfalls & Best Practices

- **Ensure Manual Shutdown is Invoked:** When `loadingscreen_manual_shutdown 'yes'` is used, failure to call `ShutdownLoadingScreenNui()` leaves players stuck on the loading screen forever.
