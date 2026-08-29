# FiveM ConVars (Console Variables) Guide

ConVars (Console Variables) configure FXServer settings, store global script options, and replicate server variables to clients.

## ConVar Directives in `server.cfg`

In `server.cfg`, convars are defined using standard flags:

```text
# 1. Standard Server Convar (Server-side only)
set mysql_connection_string "mysql://root:password@localhost/fivem"

# 2. Replicated Convar (Sent to all connected clients)
setr voice_use3dAudio "true"
setr my_server_mode "roleplay"

# 3. Server Info Convar (Visible in FiveM Server List browser)
sets Discord "https://discord.gg/mycommunity"
sets tags "roleplay, custom, cars"
```

## Reading ConVars in Scripts

### Server-Side Lua / C#
```lua
-- Read string convar with fallback default value
local dbUrl = GetConvar("mysql_connection_string", "default_db_url")

-- Read integer convar
local maxPlayers = GetConvarInt("sv_maxclients", 32)
```

### Client-Side Lua (Replicated ConVars)
Clients can read any convar defined with `setr` in `server.cfg` or declared via `convar_replicated` in `fxmanifest.lua`:

```lua
local is3dAudio = GetConvar("voice_use3dAudio", "false")
local serverMode = GetConvar("my_server_mode", "freeroam")
```

## Writing and Modifying ConVars at Runtime

```lua
-- Modify convar on the server
SetConvar("my_custom_setting", "new_value")

-- Set and replicate to all clients
SetConvarReplicated("my_replicated_setting", "synced_value")

-- Set server info tag
SetConvarServerInfo("Website", "https://myserver.com")
```
