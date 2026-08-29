---
title: "FiveM FXManifest Guide (fxmanifest.lua)"
description: "Complete directive reference, script entry points, NUI assets, dependencies, and metadata for fxmanifest.lua."
keywords: ["fxmanifest", "manifest", "resource manifest", "client_scripts", "server_scripts", "shared_scripts", "ui_page", "files"]
---

# FiveM FXManifest Guide (`fxmanifest.lua`)

The resource manifest (`fxmanifest.lua`) defines metadata, dependencies, script entry points, and streaming files for a FiveM resource.

## 1. Quick Reference & Directive Table

| Directive | Type | Description |
| :--- | :--- | :--- |
| `fx_version` | String | Manifest version format. Always use `'cerulean'`. |
| `game` | String | Target game: `'gta5'` or `'rdr3'`. |
| `lua54` | String | Enables Lua 5.4 engine (`'yes'`). |
| `client_scripts` | Array | Client-side scripts or compiled DLLs. |
| `server_scripts` | Array | Server-side scripts or compiled DLLs. |
| `shared_scripts` | Array | Scripts loaded on both client and server first. |
| `ui_page` | String | Path to root NUI HTML page. |
| `files` | Array | Files streamed to the client. |

## 2. Production Code Examples

```lua
fx_version 'cerulean'
game 'gta5'

name 'my-resource'
description 'A modern FiveM script resource'
version '1.0.0'
lua54 'yes'

shared_scripts {
    'config.lua',
    'shared/*.lua'
}

client_scripts {
    'client/*.lua'
}

server_scripts {
    'server/*.lua'
}

files {
    'web/dist/index.html',
    'web/dist/assets/*.*'
}

ui_page 'web/dist/index.html'
```

## 3. Pitfalls & Best Practices

- **Always declare `lua54 'yes'`:** Modern Lua 5.4 includes vector types and bitwise operators that prevent runtime syntax errors.
