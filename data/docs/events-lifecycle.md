---
title: "FiveM Events Lifecycle & Cancellation"
description: "Event emitter mechanisms, event order, cancellation via CancelEvent, and duplicate event prevention."
keywords: ["events", "cancelevent", "waseventcanceled", "addeventhandler", "event lifecycle", "event security"]
---

# FiveM Events Lifecycle & Cancellation

Events in FiveM are event emitters that support multiple listeners, network routing, and mid-execution cancellation.

## 1. Quick Reference

| Function | APISet | Description |
| :--- | :--- | :--- |
| `AddEventHandler(name, cb)` | Shared | Register a local or network event handler |
| `CancelEvent()` | Shared | Cancel event propagation to subsequent handlers |
| `WasEventCanceled()` | Shared | Check if an earlier handler canceled the event |

## 2. Production Code Examples

```lua
-- Block unauthorized chat slash commands
AddEventHandler('chatMessage', function(author, color, text)
    if string.sub(text, 1, 1) == '/' then
        CancelEvent() -- Cancel default chat broadcast
    end
end)
```

## 3. Pitfalls & Best Practices

- **Handler Execution Order:** Handlers execute in the exact order they were registered in memory.
