---
title: "Scripting in C# (.NET Runtime)"
description: "C# scripting in FiveM with CitizenFX.Core, BaseScript, async tasks, event handlers, and .csproj setup."
keywords: ["csharp", "c#", "dotnet", "netstandard", "basescript", "eventhandler", "tick", "citizenfx.core"]
---

# Scripting in C# (.NET Runtime)

FiveM supports C# using .NET Standard 2.0 with the `CitizenFX.Core.Client` and `CitizenFX.Core.Server` NuGet packages.

## 1. Quick Reference & Setup

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>netstandard2.0</TargetFramework>
    <TargetName>MyResource.Client.net</TargetName>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="CitizenFX.Core.Client" Version="1.0.*" />
  </ItemGroup>
</Project>
```

In `fxmanifest.lua`:
```lua
client_script 'bin/Release/netstandard2.0/MyResource.Client.net.dll'
```

## 2. Production Code Examples

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
            EventHandlers["myResource:notify"] += new Action<string>(OnNotify);
            Tick += OnTick;
        }

        private void OnNotify(string message)
        {
            Debug.WriteLine($"[NOTIFY]: {message}");
        }

        private async Task OnTick()
        {
            await Delay(1000); // 1-second non-blocking delay
            Vector3 pos = Game.PlayerPed.Position;
        }
    }
}
```

## 3. Pitfalls & Best Practices

- **Avoid Heavy Async Allocations in Tick Loops:** Reusing delegates and avoiding frequent LINQ inside `Tick` handlers prevents GC stutter.
