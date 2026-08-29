from fivem_mcp.docs import docs_manager
from fivem_mcp.server import search_docs, get_doc, scaffold_resource, get_fivem_doc_resource


def test_docs_manager_list_topics():
    topics = docs_manager.list_topics()
    assert len(topics) >= 5
    slugs = [t["topic"] for t in topics]
    assert "fxmanifest" in slugs
    assert "state-bags" in slugs
    assert "nui-messages" in slugs


def test_search_docs_exact_and_multiword():
    # Exact slug
    res_manifest = search_docs("fxmanifest")
    assert len(res_manifest) > 0
    assert res_manifest[0]["topic"] == "fxmanifest"

    # Multi-word
    res_nui = search_docs("nui callback fetch")
    assert len(res_nui) > 0
    assert res_nui[0]["topic"] == "nui-messages"

    # Statebags
    res_state = search_docs("state bag player")
    assert len(res_state) > 0
    assert res_state[0]["topic"] == "state-bags"


def test_get_doc_content():
    content = get_doc("fxmanifest")
    assert "fx_version 'cerulean'" in content
    assert "client_scripts" in content

    # Nonexistent topic returns error message
    not_found = get_doc("nonexistent_unknown_topic")
    assert "not found" in not_found.lower()


def test_mcp_resource_resolution():
    res = get_fivem_doc_resource("networking-events")
    assert "RegisterNetEvent" in res
    assert "TriggerClientEvent" in res

    res_missing = get_fivem_doc_resource("unknown_topic")
    assert "Not Found" in res_missing


def test_scaffold_resource_prompt():
    prompt = scaffold_resource(
        name="vehicle-keys",
        description="A key system for vehicles",
        has_client=True,
        has_server=True,
        has_ui=True,
    )
    assert "vehicle-keys" in prompt
    assert "fx_version 'cerulean'" in prompt
    assert "client_scripts" in prompt
    assert "server_scripts" in prompt
    assert "ui_page" in prompt
