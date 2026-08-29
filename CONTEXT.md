# FiveM Native API & Developer Documentation Context

Provides access, indexing, search, detailed inspection of FiveM and GTA V native functions, curated developer guides, and MCP resources for script development.

## Language

**Native**:
An engine or framework C++ function exposed to GTA V and FiveM scripting runtimes (Lua, JavaScript, C#).
_Avoid_: Native function, game function, API endpoint

**Hash**:
The unique 64-bit hexadecimal identifier (e.g. `0x43A66C31C68491C0`) representing a native function internally in the game binary.
_Avoid_: Function ID, native ID, hex code

**Namespace**:
A categorical grouping of related natives based on game subsystem (e.g., `PLAYER`, `VEHICLE`, `ENTITY`, `CFX`, `WEAPON`).
_Avoid_: Category, module, package

**APISet**:
The execution environment where a native is valid to run (`client`, `server`, or `shared`).
_Avoid_: Environment, side, runtime context

**Resource**:
A packaged FiveM module containing scripts, configuration, and assets managed by FXServer.
_Avoid_: Plugin, mod, addon, package

**Manifest**:
The `fxmanifest.lua` configuration file declaring resource metadata, script entry points, and asset dependencies.
_Avoid_: Config file, package.json, meta file

**StateBag**:
A synchronized, key-value state store attached to entities, players, or global server state.
_Avoid_: Sync table, shared variable, entity metadata

**NUI**:
Native User Interface; an embedded Chromium web view rendering HTML/CSS/JS inside the game client.
_Avoid_: Webview, CEF, HTML UI

**Event**:
An asynchronous message dispatched between client and server runtimes or within the same runtime.
_Avoid_: Signal, RPC, message packet

**Client**:
The FiveM game instance running on the player machine executing client-side scripts.
_Avoid_: Frontend, player client

**Server**:
The FiveM server daemon (FXServer) executing server-side authoritative scripts.
_Avoid_: Backend, host, FXServer

**Signature**:
The formal declaration of a native including its name, ordered typed parameters, and return type.
_Avoid_: Declaration, prototype, function definition
