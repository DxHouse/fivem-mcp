import time
from fivem_mcp.natives import natives_manager


def run_benchmark():
    print("=== Running FiveM Natives Search Engine Benchmark ===")
    
    # 1. Verification queries
    test_queries = [
        ("GET_PLAYER_PED", "Exact Name"),
        ("0x43A66C31C68491C0", "Exact Hash"),
        ("player coords", "Multi-word (Player + Coords)"),
        ("vehicle speed", "Multi-word (Vehicle + Speed)"),
        ("entity health", "Multi-word (Entity + Health)"),
        ("create ped", "Multi-word (Create + Ped)"),
    ]

    for query, desc in test_queries:
        t0 = time.perf_counter()
        results = natives_manager.search(query, limit=5)
        dur_us = (time.perf_counter() - t0) * 1_000_000
        first = results[0]["name"] if results else "None"
        print(f"[{desc:30}] '{query}' -> Top: {first:30} ({dur_us:.1f} us)")

    # 2. 500 iterations batch latency test
    iterations = 500
    queries_pool = ["player", "vehicle", "entity", "health", "coords", "0xEEF059FAD016D209", "GET_PLAYER_PED", "create object"]
    
    t0 = time.perf_counter()
    for i in range(iterations):
        q = queries_pool[i % len(queries_pool)]
        natives_manager.search(q, limit=10)
    total_time = time.perf_counter() - t0
    avg_latency_ms = (total_time / iterations) * 1000
    avg_latency_us = avg_latency_ms * 1000

    # 3. Validator benchmark
    sample_script = """
    RegisterNetEvent('shop:purchase', function(item, amount)
        local src = source
        local coords = GetEntityCoords(GetPlayerPed(src))
        if #(coords - vector3(0, 0, 0)) < 5.0 then
            -- clean code
        end
    end)
    """
    from fivem_mcp.validator import script_validator
    t0 = time.perf_counter()
    for _ in range(500):
        script_validator.validate(sample_script)
    val_total = time.perf_counter() - t0
    val_avg_ms = (val_total / 500) * 1000
    print(f"500 Validator Scans Total: {val_total:.4f} s | Avg: {val_avg_ms:.4f} ms ({val_avg_ms * 1000:.1f} us)")
    print("-" * 60)

    assert avg_latency_ms < 0.15, f"Benchmark failed: average latency {avg_latency_ms:.4f} ms >= 0.15 ms target"
    assert val_avg_ms < 1.0, f"Validator failed: average latency {val_avg_ms:.4f} ms >= 1.0 ms target"
    print("[PASS] All performance targets passed successfully!")


if __name__ == "__main__":
    run_benchmark()
