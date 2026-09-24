---
title: "Low-Level Game Events (gameEventTriggered) Reference"
description: "Intercepting native GTA V C++ engine events for damage, death, and vehicle destruction via gameEventTriggered."
keywords: ["game events", "gameeventtriggered", "ceventnetworkentitydamage", "ceventnetworkplayerdeath", "damage", "combat", "kills"]
---

# Low-Level Game Events (`gameEventTriggered`) Reference

`gameEventTriggered` intercepts native GTA V C++ engine events dispatched whenever entities take damage, vehicles are destroyed, or players die.

## 1. Quick Reference & Event Schema

| Event Name | Dispatched When | Args Array Schema |
| :--- | :--- | :--- |
| `CEventNetworkEntityDamage` | Entity takes damage | `args[1]` = victim handle<br>`args[2]` = attacker handle<br>`args[6]` = fatal flag (1/0)<br>`args[7]` = weapon hash |
| `CEventNetworkPlayerDeath` | Networked player dies | `args[1]` = victim player ped<br>`args[2]` = killer entity |

## 2. Production Code Examples

```lua
AddEventHandler('gameEventTriggered', function(name, args)
    if name == 'CEventNetworkEntityDamage' then
        local victim = args[1]
        local attacker = args[2]
        local isFatal = args[6] == 1
        local weaponHash = args[7]

        if victim == PlayerPedId() then
            print(string.format("Damage from attacker %s (Weapon: 0x%X, Fatal: %s)", attacker, weaponHash, isFatal))
        end
    end
end)
```

## 3. Pitfalls & Best Practices

- **Filter by Local Ped:** `gameEventTriggered` fires for ambient NPC damage as well; always check `victim == PlayerPedId()` if you only care about local player events.
