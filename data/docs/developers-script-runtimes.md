# Script Runtimes Architecture & Serialization Overhead

FiveM natively hosts three distinct scripting runtimes: Lua 5.4, JavaScript / TypeScript (V8), and C# (.NET/Mono).

## Runtime Comparison Matrix

| Runtime | Engine | Strengths | Ideal Use Case |
| :--- | :--- | :--- | :--- |
| **Lua 5.4** | Custom C/C++ VM | Zero memory overhead, fastest native calls, instant reload | Core gameplay loops, HUD, entity control (~90% of resources) |
| **JavaScript / TS** | V8 (Node.js backend) | Rich NPM ecosystem, asynchronous event handling, TypeScript | Database drivers, WebSockets, Discord bots, JSON processing |
| **C# (.NET)** | Mono / .NET Standard 2.0 | Strong typing, OOP architecture, high math performance | Complex vehicle mechanics, physics engines, enterprise frameworks |

## Cross-Runtime Serialization (`msgpack`)

When invoking `exports` or triggering events across different runtimes (e.g. Lua calling a C# export or JavaScript triggering a Lua event):
1. Parameters must be serialized into **MessagePack (`msgpack`)** binary format.
2. The receiving runtime deserializes the binary payload into its internal object representation.

### Performance Tip: Minimize Cross-Language Exports in Tight Loops
- In a `Wait(0)` frame tick loop, calling an export in a different language costs **5x to 20x** more CPU time than calling a local function within the same runtime due to msgpack serialization.
- Cache export results locally or keep hot tick math inside a single runtime.
