---
title: "FiveM ConVars (Console Variables) Guide"
description: "Configuring FXServer with ConVars, replication flags (setr), server info (sets), and server.cfg integration."
keywords: ["convars", "setr", "sets", "getconvar", "setconvar", "server.cfg", "convar_replicated"]
---

# FiveM ConVars (Console Variables) Guide

ConVars (Console Variables) configure FXServer settings, store global script options, and replicate server variables to clients.

## 1. Quick Reference & Directives

| Directive / Flag | Scope | Description |
| :--- | :--- | :--- |
| `set <name> <val>` | Server-only | Standard internal server convar |
| `setr <name> <val>` | Replicated | Replicated automatically to all client instances |
| `sets <name> <val>` | Server List Info | Displayed publicly in FiveM Server List |

## 2. Production Code Examples

```lua
-- SERVER SIDE: Reading and writing convars
local dbUrl = GetConvar("mysql_connection_string", "default_db_url")
SetConvarReplicated("voice_use3dAudio", "true")

-- CLIENT SIDE: Reading replicated convar
local is3dAudio = GetConvar("voice_use3dAudio", "false")
```

## 3. Pitfalls & Best Practices

- **Never put credentials in `setr`:** `setr` values are sent to all connected players; database passwords must strictly use `set`.
