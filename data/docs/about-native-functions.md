# FiveM Native Functions Guide

Native functions are C++ game engine functions exposed by FiveM/GTA V for script execution.

## Anatomy of a Native

Every native has:
1. **Name**: Human-readable identifier (e.g. `GET_PLAYER_PED`, `SET_ENTITY_COORDS`).
2. **Hash**: 64-bit hex hash (e.g. `0x43A66C31C68491C0`) identifying the function internally in the game binary.
3. **Namespace**: Category of the native subsystem (e.g. `PLAYER`, `VEHICLE`, `ENTITY`, `CFX`).
4. **APISet**: Execution environment (`client`, `server`, or `shared`).

## Calling Conventions in Different Runtimes

### Lua Calling Convention
In Lua, native functions can be called in `PascalCase`, `camelCase`, or `ALL_CAPS`:

```lua
-- All three invoke the exact same native internally:
local ped = GetPlayerPed(-1)
local ped = getPlayerPed(-1)
local ped = GET_PLAYER_PED(-1)
```

### Pointer and Multiple Return Values in Lua
In GTA V C++, many natives return values by writing into pointer parameters (e.g., `BOOL GET_GROUND_Z_FOR_3D_COORD(float x, float y, float z, float *groundZ, BOOL ignoreWater)`).

In Lua, FiveM automatically converts pointer arguments into **multiple return values**:

```lua
-- Lua receives the return value AND output pointer values:
local success, groundZ = GetGroundZFor_3dCoord(x, y, z, false)
if success then
    print("Ground Z is:", groundZ)
end
```

### C# Calling Convention
In C#, natives are strongly typed and located under `CitizenFX.Core.Native.API`:

```csharp
using CitizenFX.Core;
using static CitizenFX.Core.Native.API;

int playerPed = GetPlayerPed(-1);
```

## CFX Namespaces (FiveM Specific Extensions)
Natives under the `CFX` namespace are custom additions made by FiveM (not in standard GTA V):
- `CreateDui`, `SetNuiFocus`, `TriggerLatentClientEvent`, `GetPlayerPing`, `PerformHttpRequest`
