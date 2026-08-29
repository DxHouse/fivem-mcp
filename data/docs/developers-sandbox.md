# FiveM Scripting Security Sandbox

FiveM employs an isolated sandbox model to prevent malicious server resources from compromising player machines or unauthorized client scripts from modifying local operating system files.

## Client Sandbox Restrictions

On the client runtime:
1. **Forbidden Standard Libraries**:
   - `os.execute`, `os.remove`, `os.rename`, and `io.open` are stripped or restricted in Lua.
   - Raw file system access outside the resource package is completely blocked.
   - Arbitrary DLL loading (`package.loadlib`) is blocked.
2. **Safe Key-Value Storage (KVP)**:
   - To persist data on the client locally without filesystem access, use **Resource KVP** natives:
     - `SetResourceKvp(key, value)`
     - `GetResourceKvpString(key)`
     - `GetResourceKvpInt(key)`
     - `DeleteResourceKvp(key)`

## Server Sandbox & Permissions

On FXServer:
1. **Filesystem Isolation**:
   - Server scripts have full access to `SaveResourceFile(resource, path, data, length)` and `LoadResourceFile(resource, path)` within the server directory hierarchy.
   - Node.js runtime on server has full access to `fs` module, but paths should be sanitized to avoid directory traversal.
2. **ACE Security Model**:
   - Access Control Entries protect administrative natives (e.g. `ExecuteCommand`, `DropPlayer`).
   - Server console commands registered with `RegisterCommand(name, cb, true)` require explicit ACE permission grants in `server.cfg`.
