# FiveM NUI & UI Communication Guide

NUI (Native User Interface) renders HTML/CSS/JS web pages inside the FiveM game client.

## Lua to NUI Communication (`SendNUIMessage`)

Send data packets from client Lua to JavaScript:

```lua
-- Client Lua: Open UI and send data
SetNuiFocus(true, true) -- enables mouse cursor and keyboard input
SendNUIMessage({
    action = 'openMenu',
    data = {
        title = 'Inventory',
        items = { 'bread', 'water', 'bandage' }
    }
})
```

```javascript
// Web JavaScript (NUI page)
window.addEventListener('message', (event) => {
    const item = event.data;
    if (item.action === 'openMenu') {
        console.log('Opening menu with items:', item.data.items);
        document.getElementById('app').style.display = 'block';
    }
});
```

## NUI to Lua Communication (`RegisterNUICallback`)

Send POST requests from JavaScript back to client Lua:

```javascript
// Web JavaScript: Send callback back to client Lua
async function postData(endpoint, data = {}) {
    // URL format: https://<current_resource_name>/<callback_name>
    const resourceName = GetParentResourceName();
    const response = await fetch(`https://${resourceName}/${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    return await response.json();
}

// Example: closing UI
postData('closeUI', { status: 'cancelled' });
```

```lua
-- Client Lua: Handle the callback
RegisterNUICallback('closeUI', function(data, cb)
    SetNuiFocus(false, false) -- release focus
    print('UI closed with reason:', data.status)
    cb({ ok = true }) -- ALWAYS invoke cb() to finish the HTTP response!
end)
```

## NUI Checklist & Pitfalls

1. **Always Call `cb(...)`**: Every `RegisterNUICallback` handler MUST invoke the callback `cb(...)`, otherwise the browser `fetch` promise will hang indefinitely.
2. **Resource Name In Fetch**: Always use `GetParentResourceName()` in JavaScript to avoid hardcoding resource folder names.
3. **Keep `ui_page` Updated**: Ensure `ui_page` and all bundled build assets (`.js`, `.css`, images) are declared in `files { ... }` inside `fxmanifest.lua`.
