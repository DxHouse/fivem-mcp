---
title: "FiveM NUI & Web UI Communication Guide"
description: "Two-way communication between FiveM Lua and Chromium Web UI using SendNUIMessage and RegisterNUICallback."
keywords: ["nui", "cef", "webview", "html ui", "sendnuimessage", "registernuicallback", "setnuifocus", "callbacks"]
---

# FiveM NUI & Web UI Communication Guide

NUI (Native User Interface) allows developers to build user interfaces using standard web technologies (HTML, CSS, JavaScript, React, Vue).

## 1. Quick Reference

| Function | Direction | Description |
| :--- | :--- | :--- |
| `SendNUIMessage(data)` | Lua -> Web JS | Sends a JSON message envelope to the NUI window |
| `RegisterNUICallback(name, cb)` | Web JS -> Lua | Receives HTTP POST callback from `fetch()` in JS |
| `SetNuiFocus(cursor, keyboard)` | Client Lua | Toggles mouse cursor and keyboard focus |

## 2. Production Code Examples

```lua
-- CLIENT LUA:
RegisterNUICallback('closeUI', function(data, cb)
    SetNuiFocus(false, false)
    cb({ ok = true }) -- ALWAYS invoke callback!
end)
```

```javascript
// NUI JS:
window.addEventListener('message', (event) => {
    if (event.data.action === 'open') {
        document.body.style.display = 'block';
    }
});

function closeMenu() {
    fetch(`https://${GetParentResourceName()}/closeUI`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({})
    });
}
```

## 3. Pitfalls & Best Practices

- **Always Invoke `cb()` in `RegisterNUICallback`:** Failing to call `cb()` causes the client Chromium `fetch()` promise to hang indefinitely.
