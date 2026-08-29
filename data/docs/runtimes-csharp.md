# Scripting in C# (.NET Runtime)

FiveM supports C# using .NET Standard with the `CitizenFX.Core.Client` and `CitizenFX.Core.Server` libraries.

## Project Configuration (`.csproj`)

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>netstandard2.0</TargetFramework>
    <DebugType>portable</DebugType>
    <TargetName>MyResource.Client.net</TargetName>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="CitizenFX.Core.Client" Version="1.0.*" />
  </ItemGroup>
</Project>
```

In `fxmanifest.lua`, specify compiled `.net.dll` files:
```lua
client_script 'bin/Release/netstandard2.0/MyResource.Client.net.dll'
server_script 'bin/Release/netstandard2.0/MyResource.Server.net.dll'
```

## Creating a Script (`BaseScript`)

All script logic extends `BaseScript`:

```csharp
using System;
using System.Threading.Tasks;
using CitizenFX.Core;
using static CitizenFX.Core.Native.API;

namespace MyResource.Client
{
    public class ClientMain : BaseScript
    {
        public ClientMain()
        {
            // Register event handlers
            EventHandlers["myResource:notify"] += new Action<string>(OnNotify);
            
            // Register tick handler
            Tick += OnTick;
        }

        private void OnNotify(string message)
        {
            Debug.WriteLine($"Notification: {message}");
        }

        private async Task OnTick()
        {
            await Delay(1000); // Non-blocking delay
            
            Vector3 playerPos = Game.PlayerPed.Position;
            // logic
        }

        [Command("getpos")]
        private void GetPosCommand()
        {
            Vector3 pos = Game.PlayerPed.Position;
            TriggerEvent("chat:addMessage", new { args = new[] { $"Position: {pos}" } });
        }
    }
}
```
