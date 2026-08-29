# 04: Automated Performance Benchmark & Verification Suite

**What to build:** An automated test and benchmark suite verifying that multi-word queries, exact hash lookups, namespace filters, and apiset filters work accurately, and measuring latency across 500+ iterations to confirm sub-0.15ms query performance.

**Blocked by:** 03: Eager Preloading & FastMCP Tools Integration

**Status:** ready-for-agent

- [x] Automated test checks multi-word search (e.g. `get player ped`, `vehicle coords`)
- [x] Automated test checks exact hash search (e.g. `0x43A66C31C68491C0`)
- [x] Automated benchmark runs 500 search queries and verifies average latency is < 0.15 ms/query
- [x] FastMCP CLI inspection passes cleanly
