from fivem_mcp.server import ping, search_natives, get_native_detail, mcp


def test_server_ping():
    assert ping("test") == "pong: test"


def test_server_search_natives():
    results = search_natives("GET_ENTITY_HEALTH", namespace="ENTITY")
    assert isinstance(results, list)
    assert len(results) > 0
    assert results[0]["name"] == "GET_ENTITY_HEALTH"


def test_server_get_native_detail():
    detail = get_native_detail("GET_ENTITY_HEALTH")
    assert isinstance(detail, dict)
    assert detail["name"] == "GET_ENTITY_HEALTH"
    assert detail["results"] == "int"

    notFound = get_native_detail("INVALID_NATIVE_12345")
    assert "not found" in notFound
