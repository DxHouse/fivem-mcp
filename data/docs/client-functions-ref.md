# Client-Side Scripting Functions Reference

FiveM provides a suite of client-side runtime functions, command helpers, key-mapping systems, and class wrappers for Lua and C#.

## Key Mapping & User Input

### `RegisterKeyMapping`
Binds a custom command to a keyboard key or controller button with player-rebindable keybindings in GTA V Settings:

```lua
-- Syntax: RegisterKeyMapping(commandName, description, defaultBindingType, defaultControl)
RegisterCommand('+openInventory', function()
    print("Opening Inventory...")
end, false)

RegisterCommand('-openInventory', function()
    print("Closed Inventory.")
end, false)

-- Bind to 'TAB' by default (rebindable in Settings -> Key Mappings -> FiveM)
RegisterKeyMapping('+openInventory', 'Open Player Inventory', 'keyboard', 'TAB')
```

## Client Lua Built-in State Wrappers

### `LocalPlayer`
Represents the local client's state and entity:

```lua
-- Local player ped handle
local ped = PlayerPedId()

-- Local player StateBag
LocalPlayer.state:set('isHandcuffed', true, true)
print("Is Handcuffed:", LocalPlayer.state.isHandcuffed)
```

## Client C# (.NET) High-Level Wrappers

In C#, `CitizenFX.Core.UI` and `CitizenFX.Core.World` provide object-oriented abstractions over natives:

```csharp
using CitizenFX.Core;
using CitizenFX.Core.UI;

// 1. Drawing Screen Notifications & Subtitles
Screen.ShowNotification("~g~Mission Completed!~s~");
Screen.ShowSubtitle("Objective: Return to headquarters.", 5000);

// 2. World & Entity Helpers
Ped playerPed = Game.PlayerPed;
Vector3 forwardPos = playerPed.GetOffsetPosition(new Vector3(0, 5, 0));
Prop spawnedBox = await World.CreateProp("prop_box_wood02a", forwardPos, true, false);

// 3. Audio & Sounds
Audio.PlaySoundFrontend("SELECT", "HUD_FRONTEND_DEFAULT_SOUNDSET");
```

## Client NUI Focus & Cursor Helpers

```lua
-- Set input focus to NUI (hasCursor, hasKeyboard)
SetNuiFocus(true, true)

-- Keep game rendering behind pause menu
SetScriptGfxDrawBehindPausemenu(true)
```
