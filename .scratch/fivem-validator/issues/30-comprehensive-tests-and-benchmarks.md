# 30: Comprehensive Test Suite & Benchmark Verification for ScriptValidator

**What to build:** Create `tests/test_validator.py` with test cases for all security, performance, native mismatch, and callback rules, verify full test suite passes 100%, and ensure validation latency is < 1 ms.

**Blocked by:** 29: FastMCP validate_script Tool Integration & Documentation

**Status:** ready-for-agent

- [x] Automated tests verify detection of `SEC001`, `SEC003`, `PERF001`, `PERF002`, `PERF003`, `BUG001`, and `BUG003`
- [x] Automated tests verify clean scripts pass with `valid: true`
- [x] Full test suite passes 100%
- [x] Validation latency validated in benchmark
