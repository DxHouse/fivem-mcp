# Low-Level Game Events (`gameEventTriggered`) Reference

`gameEventTriggered` intercepts native GTA V C++ engine events dispatched whenever entities take damage, vehicles are destroyed, or players die.

## `gameEventTriggered` Event List

| Event Name | Dispatched When | Args Array Schema |
| :--- | :--- | :--- |
| `CEventNetworkEntityDamage` | Entity takes damage | `args[1]` = victim handle<br>`args[2]` = attacker handle<br>`args[6]` = fatal flag (1/0)<br>`args[7]` = weapon hash |
| `CEventNetworkPlayerDeath` | Networked player dies | `args[1]` = victim player ped<br>`args[2]` = killer entity |
| `CEventNetworkVehicleUndrivable` | Vehicle becomes wrecked | `args[1]` = vehicle handle |
| `CEventNetworkPlayerCollectedPickup` | Player collects pickup | `args[1]` = player ped<br>`args[2]` = pickup hash |

## Complete Damage & Kill Tracking Implementation

```lua
AddEventHandler('gameEventTriggered', function(name, args)
    if name == 'CEventNetworkEntityDamage' then
        local victim = args[1]
        local attacker = args[2]
        local isFatal = args[6] == 1
        local weaponHash = args[7]

        -- Filter: Only track damage to local player
        if victim == PlayerPedId() then
            local attackerName = "Unknown"
            if IsEntityAPed(attacker) and IsPedAPlayer(attacker) then
                local attackerPlayer = NetworkGetPlayerIndexFromPed(attacker)
                attackerName = GetPlayerName(attackerPlayer)
            end

            if isFatal then
                print(string.format("Killed by: %s (Weapon: 0x%X)", attackerName, weaponHash))
                TriggerServerEvent('death:playerDied', attackerName, weaponHash)
            else
                print(string.format("Damaged by: %s (Weapon: 0x%X)", attackerName, weaponHash))
            end
        end
    end
end)
```
