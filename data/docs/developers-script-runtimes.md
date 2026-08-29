---
title: "Script Runtimes Architecture & Serialization Overhead"
description: "Internal architecture of Lua 5.4, V8 JavaScript, and C# Mono, memory models, and msgpack export serialization."
keywords: ["script runtimes", "runtimes", "msgpack", "v8", "mono", "exports", "serialization", "cross-language"]
---

# Script Runtimes Architecture & Serialization Overhead

FiveM natively hosts three distinct scripting runtimes: Lua 5.4, JavaScript / TypeScript (V8), and C# (.NET/Mono).

## 1. Quick Reference & Engine Matrix

| Runtime | Engine | Strengths | Use Case |
| :--- | :--- | :--- | :--- |
| **Lua 5.4** | Custom C/C++ VM | Lowest memory footprint, fastest native calls | Gameplay loops, HUD, entity control |
| **JavaScript / TS** | V8 (Node.js backend) | Rich NPM ecosystem, async promises, WebSockets | Database drivers, Discord bots, JSON |
| **C# (.NET)** | Mono / .NET Standard 2.0 | Strong typing, OOP architecture, high math performance | Complex vehicle physics, enterprise frameworks |

## 2. Production Performance Insights

```lua
-- Cross-runtime export calls serialize through MessagePack (msgpack):
-- Calling an export in another runtime inside a Wait(0) loop costs 5-20x more than a local call.
-- Best practice: Cache the export value outside the hot tick loop!
```

## 3. Pitfalls & Best Practices

- **Avoid Cross-Language Export Spam in Tick Loops:** Cache results or keep frame-tick logic within a single language.
