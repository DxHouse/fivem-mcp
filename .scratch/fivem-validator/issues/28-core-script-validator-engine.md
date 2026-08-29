# 28: Core ScriptValidator Engine & Static Analysis Rules & ADR 0008

**What to build:** Implement `src/fivem_mcp/validator.py` with static rule checks for security, performance, NUI callbacks, and native environment mismatches. Create `docs/adr/0008-static-script-validator.md`.

**Blocked by:** None (can start immediately)

**Status:** ready-for-agent

- [x] `src/fivem_mcp/validator.py` implements environment auto-detection (`client`, `server`, `shared`)
- [x] Security rules implemented: `SEC001` (source capture), `SEC002` (unvalidated payment/reward), `SEC003` (forbidden client OS calls)
- [x] Performance rules implemented: `PERF001` (tight Wait(0) loops), `PERF002` (GetPlayerPed(-1) in loops), `PERF003` (GetDistanceBetweenCoords)
- [x] Correctness rules implemented: `BUG001` (missing NUI callback `cb()`), `BUG002` (invalid native), `BUG003` (APISet mismatch), `BUG004` (deprecated manifest directives)
- [x] `docs/adr/0008-static-script-validator.md` created
