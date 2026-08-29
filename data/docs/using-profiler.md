---
title: "Using the FiveM Profiler"
description: "Frame-by-frame execution profiling, resmon 1 tick analysis, Chrome tracing, and Speedscope optimization."
keywords: ["profiler", "resmon", "performance", "speedscope", "chrome tracing", "lag", "tick", "cpu time"]
---

# Using the FiveM Profiler

The FiveM Profiler captures frame-by-frame execution times and resource ticks to identify script lag, micro-stutters, and CPU spikes.

## 1. Quick Reference & Commands

| Command | Environment | Description |
| :--- | :--- | :--- |
| `resmon 1` | Client F8 Console | Real-time resource CPU (ms) and memory monitor |
| `profiler record 500` | F8 / Server Console | Record detailed trace for 500 frames |
| `profiler view` | In-Game UI | Open interactive profile viewer |
| `profiler save trace.json` | F8 Console | Export JSON trace file for Speedscope / Chrome |

## 2. Production Workflow

1. Execute `profiler record 500` during gameplay or server stress.
2. Execute `profiler save my_trace.json`.
3. Open [speedscope.app](https://www.speedscope.app/) and drop `my_trace.json`.
4. Switch to **Left Heavy** view to identify hot functions consuming high aggregate CPU time.

## 3. Pitfalls & Best Practices

- **Target CPU Budget:** Idle client resources should consume **0.00 ms - 0.04 ms**. Active interaction points should rarely exceed **0.15 ms**.
