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
    get_fivem_doc_resource,
)


def test_docs_manager_all_30_topics():
    topics = docs_manager.list_topics()
    assert len(topics) == 30, f"Expected 30 topics, found {len(topics)}"
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
    ]
    for expected in expected_slugs:
        assert expected in slugs, f"Missing topic slug: {expected}"


def test_search_docs_game_references():
    test_cases = [
        ("controls input context", "game-references-controls"),
        ("blip sprites markers", "game-references-blips-markers"),
        ("hud colors formatting", "game-references-ui-hud"),
        ("vehicle models paint colors", "game-references-vehicles"),
        ("weapon hashes ped models", "game-references-weapons-peds"),
        ("radio stations ambient speech", "game-references-audio-speech"),
        ("map zones data files", "game-references-world-zones"),
        ("damage tracking entity event", "game-references-game-events"),
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
    res_controls = get_fivem_doc_resource("game-references-controls")
    assert "INPUT_CONTEXT" in res_controls

    res_blips = get_fivem_doc_resource("game-references-blips-markers")
    assert "AddBlipForCoord" in res_blips


def test_all_8_scaffolding_prompts():
    assert "fxmanifest.lua" in scaffold_resource(name="res")
    assert "RegisterNUICallback" in scaffold_nui_resource(name="nui")
    assert "CreateDui" in scaffold_dui_screen(name="tv")
    assert "CitizenFX.Core" in scaffold_csharp_resource(name="cs")
    assert "playerConnecting" in scaffold_player_connecting(name="auth")
    assert "CreateVehicleServerSetter" in scaffold_onesync_spawner(name="sync")
    
    p_inter = scaffold_interaction_point(name="shop", marker_type=1, blip_sprite=52, key_bind="E")
    assert "shop" in p_inter
    assert "DrawMarker" in p_inter
    assert "AddBlipForCoord" in p_inter

    p_dmg = scaffold_damage_tracker(name="combat-log")
    assert "combat-log" in p_dmg
    assert "CEventNetworkEntityDamage" in p_dmg
    assert "gameEventTriggered" in p_dmg
