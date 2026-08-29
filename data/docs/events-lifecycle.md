# FiveM Events Lifecycle & Cancellation

Events in FiveM are event emitters that support multiple listeners, network routing, and mid-execution cancellation.

## Listening and Handling Events

```lua
-- Local or Network event listener
AddEventHandler('chatMessage', function(author, color, text)
    print(string.format("[%s]: %s", author, text))
end)
```

## Canceling Events (`CancelEvent`)

Certain base game and framework events can be canceled by calling `CancelEvent()` within the handler. Once canceled, subsequent event listeners and default actions are aborted:

```lua
-- Example: Block specific chat messages or commands
AddEventHandler('chatMessage', function(author, color, text)
    if string.sub(text, 1, 1) == '/' then
        -- Cancel default chat broadcast for slash commands
        CancelEvent()
    end
end)

-- Checking if an event was canceled
AddEventHandler('chatMessage', function(author, color, text)
    if WasEventCanceled() then
        print("Chat message was canceled by a previous handler!")
    end
end)
```

## Event Propagation Lifecycle

1. `TriggerEvent` / Network Event is dispatched.
2. Handlers execute in the order they were registered.
3. If any handler calls `CancelEvent()`, `WasEventCanceled()` becomes `true`.
4. Handlers registered after the cancellation can choose to return early if `WasEventCanceled()` is true.

## Event Security Checklist

- Capture `local src = source` immediately in server-side `RegisterNetEvent` handlers.
- Validate that the player is within interaction distance of the target entity before executing server rewards or state changes.
