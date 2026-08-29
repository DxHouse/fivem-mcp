---
title: "FiveM Scripting Security Sandbox"
description: "Client and server execution sandboxes, filesystem restrictions, blocked OS libraries, and safe Resource KVP."
keywords: ["sandbox", "security", "kvp", "resource kvp", "filesystem", "isolation", "os.execute", "io.open"]
---

# FiveM Scripting Security Sandbox

FiveM employs an isolated sandbox model to prevent malicious server resources from compromising player machines or unauthorized client scripts from modifying local operating system files.

## 1. Quick Reference

| Runtime | Restricted Libraries | Safe Storage Alternatives |
| :--- | :--- | :--- |
| **Client** | `os.execute`, `os.remove`, `io.open`, `package.loadlib` | `SetResourceKvp`, `GetResourceKvpString` |
| **Server** | Direct OS execution without ACE permissions | `SaveResourceFile`, `LoadResourceFile` |

## 2. Production Code Examples

```lua
-- Safe Client Persistent Storage (KVP)
SetResourceKvp("settings_volume", "85")
local savedVol = GetResourceKvpInt("settings_volume")
print("Saved volume setting:", savedVol)
```

## 3. Pitfalls & Best Practices

- **Never Attempt Raw File I/O on Client:** Use KVP or send data to server for persistent database storage.
