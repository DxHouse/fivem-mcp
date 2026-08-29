# GTA V & FiveM Controls Reference

Controls are numerical indices (0-357) used with `IsControlJustPressed`, `IsControlPressed`, and `DisableControlAction`.

## Common Control Action IDs

| Control ID | Input Name | Keyboard Default | Controller Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `0` | `INPUT_NEXT_CAMERA` | `V` | `SELECT / BACK` | Change camera view |
| `23` | `INPUT_ENTER` | `F` | `Y / TRIANGLE` | Enter / Exit vehicle |
| `24` | `INPUT_ATTACK` | `LMB` | `RT / R2` | Attack / Fire weapon |
| `25` | `INPUT_AIM` | `RMB` | `LT / L2` | Aim weapon |
| `38` | `INPUT_CONTEXT` | `E` | `DPAD_RIGHT` | Primary context interaction |
| `44` | `INPUT_COVER` | `Q` | `RB / R1` | Take cover |
| `47` | `INPUT_DETONATE` | `G` | `DPAD_LEFT` | Throw grenade / Detonate |
| `71` | `INPUT_VEH_ACCELERATE`| `W` | `RT / R2` | Vehicle Accelerate |
| `72` | `INPUT_VEH_BRAKE` | `S` | `LT / L2` | Vehicle Brake / Reverse |
| `75` | `INPUT_VEH_EXIT` | `F` | `Y / TRIANGLE` | Exit vehicle |
| `86` | `INPUT_VEH_HORN` | `E` | `L3 (Thumbstick)` | Vehicle Horn / Siren |
| `177` | `INPUT_CELLPHONE_CANCEL`| `BACKSPACE` | `B / CIRCLE` | Phone Cancel / Back |
| `199` | `INPUT_FRONTEND_PAUSE`| `P` | `START` | Pause menu |
| `288` | `INPUT_REPLAY_START_STOP_RECORDING` | `F1` | - | Replay recording |

## Input Groups (Pad Indices)
- `0`: Default gameplay controls (Player on-foot or in vehicle)
- `2`: Wheel / Frontend / UI controls

## Code Examples

```lua
-- 1. Check if player pressed [E] (INPUT_CONTEXT)
if IsControlJustPressed(0, 38) then
    print("Player interacted with [E]")
end

-- 2. Disable attacking and jumping while in a menu
CreateThread(function()
    while isMenuOpen do
        Wait(0)
        DisableControlAction(0, 24, true) -- Attack
        DisableControlAction(0, 22, true) -- Jump
        DisableControlAction(0, 75, true) -- Exit Vehicle
    end
end)
```
