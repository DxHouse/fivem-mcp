import pytest
from fivem_mcp.natives import NativesManager


@pytest.fixture(scope="module")
def manager():
    mgr = NativesManager()
    mgr.load()
    return mgr


def test_exact_name_search(manager):
    results = manager.search("GET_PLAYER_PED", limit=5)
    assert len(results) > 0
    assert results[0]["name"] == "GET_PLAYER_PED"
    assert results[0]["hash"] == "0x43A66C31C68491C0"


def test_exact_hash_search(manager):
    results = manager.search("0x43A66C31C68491C0", limit=5)
    assert len(results) > 0
    assert results[0]["name"] == "GET_PLAYER_PED"


def test_multi_word_search(manager):
    results = manager.search("player coords", limit=10)
    assert len(results) > 0
    names = [r["name"] for r in results]
    # Should include coordinate or player related functions
    assert any("COORDS" in name or "PLAYER" in name for name in names)


def test_namespace_filter(manager):
    results = manager.search("coords", namespace="ENTITY", limit=5)
    assert len(results) > 0
    for r in results:
        assert r["namespace"] == "ENTITY"


def test_apiset_filter(manager):
    results = manager.search("player", apiset="client", limit=10)
    assert len(results) > 0
    for r in results:
        assert r["apiset"] in ("client", "shared")


def test_get_detail_by_name_and_hash(manager):
    detail_by_name = manager.get_detail("GET_PLAYER_PED")
    assert detail_by_name is not None
    assert detail_by_name["name"] == "GET_PLAYER_PED"

    detail_by_hash = manager.get_detail("0x43A66C31C68491C0")
    assert detail_by_hash is not None
    assert detail_by_hash["name"] == "GET_PLAYER_PED"


def test_nonexistent_query(manager):
    results = manager.search("nonexistent_random_xyz_query_12345", limit=5)
    assert len(results) == 0
    assert manager.get_detail("nonexistent_native_xyz") is None
