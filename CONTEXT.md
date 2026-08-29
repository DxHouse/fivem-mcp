# FiveM Native API Context

Provides access, indexing, search, and detailed inspection of FiveM and GTA V native functions for script development.

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

**Client**:
The FiveM game instance running on the player machine executing client-side scripts.
_Avoid_: Frontend, player client

**Server**:
The FiveM server daemon (FXServer) executing server-side authoritative scripts.
_Avoid_: Backend, host, FXServer

**Signature**:
The formal declaration of a native including its name, ordered typed parameters, and return type.
_Avoid_: Declaration, prototype, function definition
