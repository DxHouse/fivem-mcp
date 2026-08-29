# 0008: Static Script Validator & Linter Engine

We implemented `ScriptValidator` in `src/fivem_mcp/validator.py` to provide automated static analysis and security auditing for FiveM Lua scripts. The engine detects missing `source` closures in server events (`SEC001`), forbidden client OS calls (`SEC003`), tight `Wait(0)` infinite loops (`PERF001`), legacy `GetPlayerPed(-1)` calls (`PERF002`), missing NUI `cb()` callbacks (`BUG001`), and APISet execution environment mismatches (`BUG003`).
