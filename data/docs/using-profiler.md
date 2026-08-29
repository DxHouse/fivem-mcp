# Using the FiveM Profiler

The FiveM Profiler captures frame-by-frame execution times and resource ticks to identify script lag, micro-stutters, and high CPU usage.

## Basic vs Advanced Performance Monitoring

1. **Resource Monitor (`resmon 1` in client console / F8):**
   - Shows CPU time (ms) and memory footprint (MB) per resource in real-time.
   - Ideal baseline: **0.00 ms - 0.04 ms** for idle resources.
   - Any resource exceeding **0.20 ms** continuously should be investigated.

2. **FiveM Profiler (Frame-Level Tracing):**
   - Records detailed call graphs and function execution durations across all frames.

## Recording a Profile Trace

Run commands in the client F8 console or server console:

```text
# 1. Start recording (will record 500 frames)
profiler record 500

# 2. View results in the in-game UI
profiler view

# 3. Or save to disk for Chrome Tracing analysis
profiler save my_trace.json
```

## Analyzing Traces with Speedscope or Chrome Tracing

1. Open [speedscope.app](https://www.speedscope.app/) or navigate to `chrome://tracing` in Google Chrome.
2. Drag and drop the saved `my_trace.json` file.
3. Switch to **Time Order** or **Left Heavy** view.
4. Look for:
   - Long tick blocks (`Citizen::CreateThread` taking > 1.0 ms).
   - Expensive native calls executed inside loops without sleeping (e.g. repeated `GetEntityCoords` or `DrawMarker`).
   - Deep nested table iterations.
