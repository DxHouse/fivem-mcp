# FiveM FXManifest Guide (`fxmanifest.lua`)

The resource manifest (`fxmanifest.lua`) defines metadata, dependencies, script entry points, and streaming files for a FiveM resource.

## Standard Directives

```lua
-- Modern recommended manifest format
fx_version 'cerulean'
game 'gta5'

name 'my-resource'
author 'Developer Name'
description 'A modern FiveM script resource'
version '1.0.0'

-- Enable Lua 5.4 support (strongly recommended)
lua54 'yes'

-- Shared scripts (loaded on both client and server first)
shared_scripts {
    '@ox_lib/init.lua', -- optional library import
    'config.lua',
    'shared/*.lua'
}

-- Client scripts
client_scripts {
    'client/main.lua',
    'client/utils.lua'
}

-- Server scripts
server_scripts {
    '@oxmysql/lib/MySQL.lua', -- optional database wrapper
    'server/main.lua'
}

-- Static files & NUI assets accessible to client
files {
    'web/dist/index.html',
    'web/dist/assets/*.*',
    'data/*.json'
}

-- NUI main HTML page entry point
ui_page 'web/dist/index.html'

-- Loading screen definition (if loading screen resource)
loadingscreen 'web/loading.html'
loadingscreen_manual_shutdown 'yes'
loadingscreen_cursor 'yes'

-- Convars replicated to clients
convar_replicated 'my_setting'

-- Data files for streaming game metas
data_file 'HANDLING_FILE' 'data/handling.meta'
data_file 'VEHICLE_METADATA_FILE' 'data/vehicles.meta'

-- Dependencies (ensures these resources start before this one)
dependencies {
    'ox_lib',
    'oxmysql'
}
```

## Complete Manifest Directives Reference

| Directive | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `fx_version` | String | Manifest version format. Always use `'cerulean'`. | `fx_version 'cerulean'` |
| `game` | String | Target game: `'gta5'` or `'rdr3'` (or `'common'`). | `game 'gta5'` |
| `lua54` | String | Enables Lua 5.4 engine (`'yes'`). | `lua54 'yes'` |
| `name` / `author` / `version` | String | Resource metadata. | `name 'my-resource'` |
| `client_scripts` / `client_script` | Array / String | Lua or C# DLL scripts loaded into client runtime. | `client_scripts { 'client/*.lua' }` |
| `server_scripts` / `server_script` | Array / String | Lua or C# DLL scripts loaded into server runtime. | `server_scripts { 'server/*.lua' }` |
| `shared_scripts` / `shared_script` | Array / String | Scripts loaded into both client and server before others. | `shared_scripts { 'config.lua' }` |
| `files` / `file` | Array / String | Files streamed to the client (NUI, JSON, sounds, images). | `files { 'web/dist/**' }` |
| `ui_page` | String | Path to root NUI HTML page. | `ui_page 'web/dist/index.html'` |
| `loadingscreen` | String | Path to loading screen HTML page. | `loadingscreen 'web/index.html'` |
| `loadingscreen_manual_shutdown` | String | Prevents auto-shutdown of loading screen (`'yes'`). | `loadingscreen_manual_shutdown 'yes'` |
| `loadingscreen_cursor` | String | Enables mouse cursor during loading screen (`'yes'`). | `loadingscreen_cursor 'yes'` |
| `convar_replicated` | String | Names a server convar that should be replicated to clients. | `convar_replicated 'voice_use3dAudio'` |
| `data_file` | String Pair | Mounts GTA V XML/meta files into the streaming memory. | `data_file 'HANDLING_FILE' 'handling.meta'` |
| `dependency` / `dependencies` | Array / String | Enforces resource start order. | `dependencies { 'ox_lib' }` |
| `provide` | String | Declares a virtual resource provided by this package. | `provide 'mysql-async'` |
