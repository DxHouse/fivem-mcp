---
title: "Direct-Rendered UI (DUI 3D In-Game Screens)"
description: "Rendering web pages and browser views onto 3D in-game meshes, TVs, and billboards using CreateDui."
keywords: ["dui", "createdui", "render target", "3d screen", "webview", "billboard", "tvscreen"]
---

# Direct-Rendered UI (DUI 3D In-Game Screens)

DUI allows developers to render web pages directly onto in-game 3D world models, televisions, cinema screens, billboards, and computer terminals.

## 1. Quick Reference

| Function | Description |
| :--- | :--- |
| `CreateDui(url, width, height)` | Creates offscreen Chromium browser |
| `GetDuiHandle(duiObject)` | Gets GPU texture handle |
| `CreateRuntimeTextureFromDuiHandle(txd, name, handle)` | Maps DUI onto game texture |
| `DestroyDui(duiObject)` | Destroys DUI and releases GPU memory |

## 2. Production Code Examples

```lua
local duiObject = CreateDui('https://www.youtube.com', 1280, 720)
local duiHandle = GetDuiHandle(duiObject)
local txd = CreateRuntimeTxd("dui_screen_txd")
CreateRuntimeTextureFromDuiHandle(txd, "dui_screen_tex", duiHandle)
```

## 3. Pitfalls & Best Practices

- **Always Destroy on Resource Stop:** Never leave un-destroyed DUI objects when stopping resources to prevent VRAM memory leaks.
