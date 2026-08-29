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
    scaffold_interaction_point,
    scaffold_damage_tracker,
    scaffold_secure_event_handler,
    scaffold_safe_transaction,
    get_fivem_doc_resource,
)


def test_docs_manager_all_33_topics():
    topics = docs_manager.list_topics()
    assert len(topics) == 33, f"Expected 33 topics, found {len(topics)}"
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
        "game-references-controls",
        "game-references-blips-markers",
        "game-references-ui-hud",
        "game-references-vehicles",
        "game-references-weapons-peds",
        "game-references-audio-speech",
        "game-references-world-zones",
        "game-references-game-events",
        "developers-sandbox",
        "developers-script-runtimes",
        "developers-server-security",
    ]
    for expected in expected_slugs:
        assert expected in slugs, f"Missing topic slug: {expected}"


def test_search_docs_developer_guides():
    test_cases = [
        ("sandbox security kvp", "developers-sandbox"),
        ("script runtimes msgpack v8", "developers-script-runtimes"),
        ("server security rate limit distance", "developers-server-security"),
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
    res_sandbox = get_fivem_doc_resource("developers-sandbox")
    assert "Resource KVP" in res_sandbox

    res_sec = get_fivem_doc_resource("developers-server-security")
    assert "Distance Verification" in res_sec


def test_all_10_scaffolding_prompts():
    assert "fxmanifest.lua" in scaffold_resource(name="res")
    assert "RegisterNUICallback" in scaffold_nui_resource(name="nui")
    assert "CreateDui" in scaffold_dui_screen(name="tv")
    assert "CitizenFX.Core" in scaffold_csharp_resource(name="cs")
    assert "playerConnecting" in scaffold_player_connecting(name="auth")
    assert "CreateVehicleServerSetter" in scaffold_onesync_spawner(name="sync")
    assert "DrawMarker" in scaffold_interaction_point(name="shop")
    assert "CEventNetworkEntityDamage" in scaffold_damage_tracker(name="combat-log")

    p_sec = scaffold_secure_event_handler(name="reward", cooldown_ms=5000, max_distance=3.5)
    assert "reward" in p_sec
    assert "source" in p_sec
    assert "5000" in p_sec
    assert "3.5" in p_sec

    p_tx = scaffold_safe_transaction(name="bank-transfer")
    assert "bank-transfer" in p_tx
    assert "transactionLocks" in p_tx
