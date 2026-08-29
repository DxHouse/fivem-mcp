# 21: Developer Docs (Sandbox, Script Runtimes & Server Security) & ADR 0006

**What to build:** Create comprehensive reference guides for the FiveM Security Sandbox, Script Runtimes Architecture (Lua vs V8 vs C#), and Server Event Security. Update `CONTEXT.md` with new domain terms and create `docs/adr/0006-developer-security-and-runtimes.md`.

**Blocked by:** None (can start immediately)

**Status:** ready-for-agent

- [x] `data/docs/developers-sandbox.md` covers sandbox isolation, client OS call restrictions, and safe storage
- [x] `data/docs/developers-script-runtimes.md` covers Lua 5.4, V8, C# Mono, memory models, and msgpack export serialization overhead
- [x] `data/docs/developers-server-security.md` covers threat modeling, trust boundaries, `source` verification, distance & rate-limit validation
- [x] `CONTEXT.md` updated with `Sandbox`, `Msgpack`, `TrustBoundary`, and `RateLimiter`
- [x] `docs/adr/0006-developer-security-and-runtimes.md` created
