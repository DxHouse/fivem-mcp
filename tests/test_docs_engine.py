from fivem_mcp.docs import docs_manager
from fivem_mcp.server import (
    search_docs,
    get_doc,
    scaffold_resource,
    scaffold_nui_resource,
    scaffold_dui_screen,
    scaffold_csharp_resource,
    scaffold_player_connecting,
    scaffold_onesync_spawner,
    get_fivem_doc_resource,
)


def test_docs_manager_all_22_topics():
    topics = docs_manager.list_topics()
    assert len(topics) == 22, f"Expected 22 topics, found {len(topics)}"
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
        "client-functions-ref",
        "server-functions-ref",
        "events-catalog",
        "convars",
        "onesync-routing-buckets",
    ]
    for expected in expected_slugs:
        assert expected in slugs, f"Missing topic slug: {expected}"


def test_search_docs_scripting_ref():
    test_cases = [
        ("deferrals player connecting", "events-catalog"),
        ("convar replicated server info", "convars"),
        ("onesync server setter routing bucket", "onesync-routing-buckets"),
        ("client key mapping command", "client-functions-ref"),
        ("server ace allowed identifiers", "server-functions-ref"),
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
    res_events = get_fivem_doc_resource("events-catalog")
    assert "playerConnecting" in res_events
    assert "gameEventTriggered" in res_events

    res_onesync = get_fivem_doc_resource("onesync-routing-buckets")
    assert "CreateVehicleServerSetter" in res_onesync
    assert "SetPlayerRoutingBucket" in res_onesync


def test_all_6_scaffolding_prompts():
    p_gen = scaffold_resource(name="test-resource", description="General test")
    assert "test-resource" in p_gen

    p_nui = scaffold_nui_resource(name="test-nui", description="NUI test", framework="react")
    assert "test-nui" in p_nui

    p_dui = scaffold_dui_screen(name="test-tv", url="https://example.com", target_model="prop_tv_flat_01")
    assert "test-tv" in p_dui

    p_cs = scaffold_csharp_resource(name="TestCSharp", description="C# Test")
    assert "TestCSharp" in p_cs

    p_conn = scaffold_player_connecting(name="custom-auth")
    assert "custom-auth" in p_conn
    assert "playerConnecting" in p_conn
    assert "deferrals.defer()" in p_conn

    p_sync = scaffold_onesync_spawner(name="car-spawner", entity_type="automobile")
    assert "car-spawner" in p_sync
    assert "CreateVehicleServerSetter" in p_sync
    assert "SetPlayerRoutingBucket" in p_sync
