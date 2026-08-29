# 08: Automated Test Suite for Docs & Prompt Verification

**What to build:** An automated test suite in `tests/test_docs_engine.py` validating that doc search, topic retrieval, resource resolution, and prompt generation execute accurately without errors.

**Blocked by:** 07: FastMCP Tools, Resources & Scaffolding Prompt Integration

**Status:** ready-for-agent

- [x] Automated tests verify `search_docs` multi-word and keyword matching
- [x] Automated tests verify `get_doc` returns expected Markdown content
- [x] Automated tests verify `scaffold_resource` prompt generation includes required manifest directives
- [x] Full test suite passes 100%
