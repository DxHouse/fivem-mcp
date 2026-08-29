# Server-Side Scripting Functions Reference

FXServer provides server-side runtime functions for player lifecycle management, HTTP requests, ACE permissions, and console commands.

## Player Iteration & Management

### `GetPlayers()`
Returns an array of string player IDs (`source` values) for all connected clients:

```lua
local players = GetPlayers()
for _, src in ipairs(players) do
    local playerName = GetPlayerName(src)
    local ping = GetPlayerPing(src)
    print(string.format("Player [%s] %s - Ping: %d ms", src, playerName, ping))
end
```

### `GetPlayerIdentifiers(source)`
Retrieves an array of all platform identifiers linked to the player (License, Discord, Steam, IP, FiveM):

```lua
local identifiers = GetPlayerIdentifiers(source)
for _, id in ipairs(identifiers) do
    if string.find(id, "license:") then
        print("Rockstar License:", id)
    elseif string.find(id, "discord:") then
        print("Discord ID:", id)
    end
end
```

### `DropPlayer(source, reason)`
Disconnects a client with a custom kick/ban reason:

```lua
DropPlayer(source, "Banned: Exploiting network triggers.")
```

## HTTP Networking (`PerformHttpRequest`)

Performs an asynchronous HTTP GET, POST, or PUT request from the server:

```lua
PerformHttpRequest("https://api.github.com/repos/citizenfx/fivem", function(statusCode, responseText, headers)
    if statusCode == 200 then
        local data = json.decode(responseText)
        print("Repo name:", data.name, "Stars:", data.stargazers_count)
    else
        print("HTTP request failed with status:", statusCode)
    end
end, "GET", "", { ["User-Agent"] = "FiveM-Server" })
```

## ACE Permissions & Commands

FiveM uses Access Control Entries (ACE) defined in `server.cfg`:

```lua
-- Check if player has permission
if IsPlayerAceAllowed(source, "command.admin") then
    print("Player is admin!")
end

-- Register a restricted server command (restricted=true)
RegisterCommand("kickplayer", function(source, args, rawCommand)
    local targetId = args[1]
    DropPlayer(targetId, "Kicked by administrator.")
end, true) -- true requires 'command.kickplayer' ACE permission
```

## Server C# (`CitizenFX.Core.Server`) PlayerList

In C#, connected players can be accessed via `Players`:

```csharp
using CitizenFX.Core;

public class ServerMain : BaseScript
{
    public void Announce(string msg)
    {
        foreach (Player p in Players)
        {
            p.TriggerEvent("chat:addMessage", new { args = new[] { "[SERVER]", msg } });
        }
    }
}
```
