# 0009: Modular Rule Engine Architecture for Script Validation

We refactored `ScriptValidator` in `src/fivem_mcp/validator.py` from a monolithic procedural loop into a deep Rule Engine with an internal rule seam. Each static diagnostic rule (`SEC001`, `SEC003`, `PERF001`, `PERF002`, `PERF003`, `BUG001`, `BUG003`) is isolated as a stateless predicate function accepting a pre-parsed `ScriptContext`.

This provides:
1. **Locality**: Each lint rule's detection patterns, severity, message, and remediation live entirely in one bounded function.
2. **Leverage**: The orchestrator handles line pre-parsing, environment filtering, issue sorting, and diagnostic summarization once across all rules.
3. **Testability**: Individual rules can be verified in isolation using synthetic `ScriptContext` fixtures, and custom rules can be injected via the `rules` parameter without modifying engine internals.
