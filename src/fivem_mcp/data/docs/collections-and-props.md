---
title: "Components and Props Using Collections"
description: "Managing character customization, clothing DLC packs, and attached props using collection hashes."
keywords: ["collections", "clothing", "props", "drawables", "mpheist4", "mpsecurity", "setpedcomponentvariationbycollection"]
---

# Components and Props Using Collections

In modern GTA V builds, drawable variations and attached props are addressed via explicit **Collections** to avoid legacy integer ID limits.

## 1. Quick Reference

| Function | Description |
| :--- | :--- |
| `SetPedComponentVariationByCollection(...)` | Sets drawable clothing piece by collection hash |
| `SetPedPropIndexByCollection(...)` | Sets attached prop (hat, glasses) by collection hash |
| `DoesCollectionExist(hash)` | Validates collection existence in memory |

## 2. Production Code Examples

```lua
local ped = PlayerPedId()
local componentId = 4 -- Pants
local collectionHash = `mp_m_freemode_01_mp_m_security`
local drawableHash = `mp_m_freemode_01_mp_m_security_p04`
SetPedComponentVariationByCollection(ped, componentId, collectionHash, drawableHash, 0)
```

## 3. Pitfalls & Best Practices

- **Validate DLC Packs:** Always check `DoesCollectionExist(collectionHash)` before setting clothing to prevent invisible character models.
