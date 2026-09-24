---
title: "GTA V & FiveM Controls Reference"
description: "Numerical control action IDs (0-357), input groups, key mappings, and DisableControlAction usage."
keywords: ["controls", "keybind", "input_context", "keys", "disablecontrolaction", "iscontroljustpressed", "input"]
---

# GTA V & FiveM Controls Reference

Controls are numerical indices (0-357) used with `IsControlJustPressed`, `IsControlPressed`, and `DisableControlAction`.

## 1. Quick Reference & Common Control IDs

| Control ID | Input Name | Default Key | Controller Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `23` | `INPUT_ENTER` | `F` | `Y / TRIANGLE` | Enter / Exit vehicle |
| `24` | `INPUT_ATTACK` | `LMB` | `RT / R2` | Attack / Fire weapon |
| `38` | `INPUT_CONTEXT` | `E` | `DPAD_RIGHT` | Primary context interaction |
| `47` | `INPUT_DETONATE` | `G` | `DPAD_LEFT` | Throw grenade / Detonate |
| `71` | `INPUT_VEH_ACCELERATE` | `W` | `RT / R2` | Vehicle Accelerate |
| `72` | `INPUT_VEH_BRAKE` | `S` | `LT / L2` | Vehicle Brake / Reverse |
| `75` | `INPUT_VEH_EXIT` | `F` | `Y / TRIANGLE` | Exit vehicle |
| `177` | `INPUT_CELLPHONE_CANCEL` | `BACKSPACE` | `B / CIRCLE` | Phone Cancel / Back |

## 2. Production Code Examples

```lua
-- 1. Check if player pressed [E] (INPUT_CONTEXT)
if IsControlJustPressed(0, 38) then
    print("Interacted via [E]")
end

-- 2. Disable attacking while interacting with a menu
CreateThread(function()
    while isMenuOpen do
        Wait(0)
        DisableControlAction(0, 24, true) -- Attack
        DisableControlAction(0, 75, true) -- Exit Vehicle
    end
end)
```

## 3. Pitfalls & Best Practices

- **Use `DisableControlAction` inside a `Wait(0)` loop:** Disabling controls only lasts for the current game frame.
