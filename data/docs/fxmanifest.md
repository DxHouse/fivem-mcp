# FiveM FXManifest Guide (`fxmanifest.lua`)

The resource manifest (`fxmanifest.lua`) defines metadata, dependencies, and script entry points for a FiveM resource.

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

-- Dependencies (ensures these resources start before this one)
dependencies {
    'ox_lib'
}
```

## Key Directives Reference

| Directive | Description | Example |
| :--- | :--- | :--- |
| `fx_version` | Manifest format version. Always use `'cerulean'`. | `fx_version 'cerulean'` |
| `game` | Target game. Use `'gta5'` (or `'rdr3'` for RedM). | `game 'gta5'` |
| `lua54` | Enables standard Lua 5.4 features (integers, bitwise ops, const/close). | `lua54 'yes'` |
| `client_scripts` | List of scripts executed on the client environment. | `client_scripts { 'client/*.lua' }` |
| `server_scripts` | List of scripts executed on the FXServer server environment. | `server_scripts { 'server/*.lua' }` |
| `shared_scripts` | Scripts loaded into both client and server before other files. | `shared_scripts { 'config.lua' }` |
| `files` | Assets that need to be streamed to the client (NUI, JSON, sounds). | `files { 'html/**' }` |
| `ui_page` | Defines the root HTML page for NUI. | `ui_page 'html/index.html'` |
| `dependency` / `dependencies` | Resources required to start before this resource. | `dependencies { 'oxmysql' }` |
