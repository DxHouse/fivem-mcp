from fivem_mcp.docs import docs_manager
from fivem_mcp.server import (
    search_docs,
    get_doc,
    scaffold_resource,
    scaffold_nui_resource,
    scaffold_dui_screen,
    scaffold_csharp_resource,
    get_fivem_doc_resource,
)


def test_docs_manager_all_17_topics():
    topics = docs_manager.list_topics()
    assert len(topics) == 17, f"Expected 17 topics, found {len(topics)}"
    slugs = [t["topic"] for t in topics]

    expected_slugs = [
        "fxmanifest",
        "networking-events",
        "state-bags",
        "nui-messages",
        "performance-best-practices",
        "about-native-functions",
        "runtimes-lua",
        "runtimes-csharp",
        "using-profiler",
        "network-ids",
        "events-lifecycle",
        "dui-3d-screens",
        "loading-screens",
        "voice-mumble",
        "scaleform",
        "collections-and-props",
        "fuel-consumption",
    ]
    for expected in expected_slugs:
        assert expected in slugs, f"Missing topic slug: {expected}"


def test_search_docs_various_queries():
    test_cases = [
        ("fxmanifest", "fxmanifest"),
        ("profiler chrome tracing", "using-profiler"),
        ("csharp basescript dotnet", "runtimes-csharp"),
        ("mumble proximity radio", "voice-mumble"),
        ("scaleform buttons movie", "scaleform"),
        ("dui texture web", "dui-3d-screens"),
        ("fuel consumption level", "fuel-consumption"),
        ("collections props drawable", "collections-and-props"),
        ("network id handle entity", "network-ids"),
        ("loading screen shutdown", "loading-screens"),
    ]
    for query, expected_slug in test_cases:
        results = search_docs(query)
        assert len(results) > 0, f"No search results for query: {query}"
        matched_slugs = [r["topic"] for r in results]
        assert expected_slug in matched_slugs, f"Query '{query}' did not match '{expected_slug}', got: {matched_slugs}"


def test_get_doc_all_topics():
    for topic_dict in docs_manager.list_topics():
        slug = topic_dict["topic"]
        content = get_doc(slug)
        assert content is not None
        assert len(content) > 100
        assert "#" in content


def test_mcp_resource_resolution():
    res = get_fivem_doc_resource("using-profiler")
    assert "profiler record" in res
    assert "speedscope" in res


def test_all_scaffolding_prompts():
    p_gen = scaffold_resource(name="test-resource", description="General test")
    assert "test-resource" in p_gen
    assert "fxmanifest.lua" in p_gen

    p_nui = scaffold_nui_resource(name="test-nui", description="NUI test", framework="react")
    assert "test-nui" in p_nui
    assert "RegisterNUICallback" in p_nui
    assert "ui_page" in p_nui

    p_dui = scaffold_dui_screen(name="test-tv", url="https://example.com", target_model="prop_tv_flat_01")
    assert "test-tv" in p_dui
    assert "CreateDui" in p_dui
    assert "prop_tv_flat_01" in p_dui

    p_cs = scaffold_csharp_resource(name="TestCSharp", description="C# Test")
    assert "TestCSharp" in p_cs
    assert "CitizenFX.Core" in p_cs
    assert "BaseScript" in p_cs
