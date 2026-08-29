# Work with Components and Props Using Collections

In modern GTA V / FiveM builds (e.g. mpheist4, mpsecurity, mptuner), drawable ped variations and attached props are organized into **Collections** rather than raw legacy component IDs.

## Why Collections?

Legacy natives like `SetPedComponentVariation` have integer limit ceilings when servers add hundreds of custom DLC clothing packs. Collection-based natives allow addressing components by their explicit collection hash.

## Collection Natives

### Setting Ped Components by Collection
```lua
local ped = PlayerPedId()
local componentId = 4 -- Legs / Pants
local collectionHash = `mp_m_freemode_01_mp_m_security`
local drawableHash = `mp_m_freemode_01_mp_m_security_p04`
local textureIndex = 0

-- Modern collection setter
SetPedComponentVariationByCollection(ped, componentId, collectionHash, drawableHash, textureIndex)
```

### Attached Props by Collection (Hats, Glasses, Helmets)
```lua
local propIndex = 0 -- Hat / Helmet
local propCollection = `mp_m_freemode_01_mp_m_security_props`
local propDrawable = `prop_helmet_01`

SetPedPropIndexByCollection(ped, propIndex, propCollection, propDrawable, 0)
```

## Validating Collections

```lua
-- Check if a collection is valid and loaded in memory
local isValid = DoesCollectionExist(collectionHash)
if isValid then
    print("Collection is available!")
end
```
