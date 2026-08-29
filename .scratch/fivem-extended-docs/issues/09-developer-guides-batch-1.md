# 09: Developer Guides Batch 1 (Runtimes, Profiling & Networking) & ADR 0003

**What to build:** Create comprehensive Markdown guides for Native functions, Lua 5.4 runtime, C# runtime, Profiler, Network IDs, and Event Lifecycles. Update `CONTEXT.md` with new domain terms and create `docs/adr/0003-extended-knowledge-base-and-templates.md`.

**Blocked by:** None (can start immediately)

**Status:** ready-for-agent

- [x] `data/docs/about-native-functions.md` covers calling conventions, pointers, hashes, and namespaces
- [x] `data/docs/runtimes-lua.md` covers Lua 5.4, vector types, metatables, and threads
- [x] `data/docs/runtimes-csharp.md` covers `CitizenFX.Core`, `BaseScript`, `[EventHandler]`, and `[Tick]`
- [x] `data/docs/using-profiler.md` covers `profiler record`, Chrome tracing, and `resmon 1`
- [x] `data/docs/network-ids.md` covers Network ID vs Local Handle conversions and ownership
- [x] `data/docs/events-lifecycle.md` covers event listening, `CancelEvent()`, and security
- [x] `CONTEXT.md` updated with `NetworkId`, `LocalHandle`, and `Profiler`
- [x] `docs/adr/0003-extended-knowledge-base-and-templates.md` created
