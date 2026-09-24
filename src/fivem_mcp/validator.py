import re
from typing import Any
from fivem_mcp.natives import natives_manager

_SERVER_INDICATORS = {
    "registerserverevent", "triggerclientevent", "triggerlatentclientevent",
    "getplayers", "dropplayer", "getplayeridentifiers", "isplayeraceallowed",
    "createvehicleserversetter", "setplayerroutingbucket", "setentityroutingbucket",
}

_CLIENT_INDICATORS = {
    "playerpedid", "setnuifocus", "sendnuimessage", "registernuicallback",
    "drawmarker", "addblipforcoord", "createdui", "registerkeymapping",
    "getentitycoords", "setentitycoords", "requestmodel",
}

_FORBIDDEN_CLIENT_FUNCS = {
    "os.execute": "os.execute is blocked on client and unsafe.",
    "os.remove": "os.remove is blocked on client.",
    "os.rename": "os.rename is blocked on client.",
    "io.open": "io.open is blocked on client. Use Resource KVP or server storage.",
    "package.loadlib": "package.loadlib is forbidden in FiveM client sandbox.",
}

_KNOWN_SERVER_ONLY_NATIVES = {
    "createvehicleserversetter", "getplayeridentifiers", "dropplayer",
    "getplayers", "isplayeraceallowed", "setplayerroutingbucket",
    "setentityroutingbucket", "saveresourcefile", "loadresourcefile",
    "getplayerping", "getplayerendpoint",
}

_KNOWN_CLIENT_ONLY_NATIVES = {
    "playerpedid", "setnuifocus", "sendnuimessage", "registernuicallback",
    "drawmarker", "addblipforcoord", "createdui", "registerkeymapping",
    "requestmodel", "hasmodelloaded", "requestscaleformmovie",
    "drawscaleformmoviefullscreen", "createcam", "renderScriptCams",
}


def detect_environment(code: str) -> str:
    """Infer execution environment (client, server, or shared) based on heuristics."""
    code_lower = code.lower()
    server_hits = sum(1 for kw in _SERVER_INDICATORS if kw in code_lower)
    client_hits = sum(1 for kw in _CLIENT_INDICATORS if kw in code_lower)
    return "server" if server_hits > client_hits else "client"


class ScriptValidator:
    """Static analysis and linter engine for FiveM Lua scripts."""

    detect_environment = staticmethod(detect_environment)

    def validate(self, code: str, environment: str = "auto") -> dict[str, Any]:
        """Perform static analysis on a FiveM Lua script and return structured diagnostics."""
        env = detect_environment(code) if environment == "auto" else environment.lower()
        issues: list[dict[str, Any]] = []
        lines = code.splitlines()

        # Context trackers
        in_loop = False
        in_loop_line = 0
        loop_has_wait_zero = False
        loop_has_distance = False
        in_nui_callback = False
        nui_callback_line = 0
        nui_has_cb = False
        in_server_event = False
        server_event_line = 0
        server_event_has_src = False

        for line_no, raw_line in enumerate(lines, start=1):
            line = raw_line.strip()
            line_lower = line.lower()

            if not line or line.startswith("--"):
                continue

            # -------------------------------------------------------------
            # Security Rule SEC003: Forbidden client OS calls
            # -------------------------------------------------------------
            if env in ("client", "auto"):
                for forbidden, reason in _FORBIDDEN_CLIENT_FUNCS.items():
                    if forbidden in line_lower:
                        issues.append({
                            "code": "SEC003",
                            "severity": "error",
                            "line": line_no,
                            "message": f"Forbidden OS library call '{forbidden}' in client environment.",
                            "recommendation": reason,
                        })

            # -------------------------------------------------------------
            # Security Rule SEC001: Missing local src = source in server event
            # -------------------------------------------------------------
            if "registernetevent(" in line_lower or "registerserverevent(" in line_lower:
                if env in ("server", "auto") or "server" in line_lower:
                    in_server_event = True
                    server_event_line = line_no
                    server_event_has_src = False

            if in_server_event:
                if re.search(r"local\s+([a-zA-Z0-9_]+)\s*=\s*source", line):
                    server_event_has_src = True
                if line == "end" or line.startswith("end)"):
                    if not server_event_has_src and "source" in code[server_event_line:]:
                        issues.append({
                            "code": "SEC001",
                            "severity": "warning",
                            "line": server_event_line,
                            "message": "Server event handler uses global 'source' without immediate local capture.",
                            "recommendation": "Capture 'local src = source' at the very beginning of the event handler closure.",
                        })
                    in_server_event = False

            # -------------------------------------------------------------
            # Performance Rule PERF002: GetPlayerPed(-1) inside loops
            # -------------------------------------------------------------
            if "getplayerped(-1)" in line_lower:
                issues.append({
                    "code": "PERF002",
                    "severity": "warning",
                    "line": line_no,
                    "message": "Use of legacy 'GetPlayerPed(-1)'.",
                    "recommendation": "Replace with modern 'PlayerPedId()' or cache entity handle once outside loop.",
                })

            # -------------------------------------------------------------
            # Performance Rule PERF003: GetDistanceBetweenCoords
            # -------------------------------------------------------------
            if "getdistancebetweencoords(" in line_lower:
                issues.append({
                    "code": "PERF003",
                    "severity": "info",
                    "line": line_no,
                    "message": "Use of legacy 'GetDistanceBetweenCoords'.",
                    "recommendation": "Replace with native vector arithmetic and length operator: '#(posA - posB)'.",
                })

            # -------------------------------------------------------------
            # Performance Rule PERF001: Tight Wait(0) loops
            # -------------------------------------------------------------
            if re.search(r"while\s+true\s+do", line_lower):
                in_loop = True
                in_loop_line = line_no
                loop_has_wait_zero = False
                loop_has_distance = False

            if in_loop:
                if re.search(r"wait\(\s*0\s*\)", line_lower) or re.search(r"citizen\.wait\(\s*0\s*\)", line_lower):
                    loop_has_wait_zero = True
                if "distance" in line_lower or "#(" in line_lower or "sleep" in line_lower:
                    loop_has_distance = True
                if line == "end" or line.startswith("end)"):
                    if loop_has_wait_zero and not loop_has_distance:
                        issues.append({
                            "code": "PERF001",
                            "severity": "warning",
                            "line": in_loop_line,
                            "message": "Tight 'while true do Wait(0)' loop without dynamic sleep or distance check.",
                            "recommendation": "Use dynamic wait: set sleep interval (e.g. 1000ms) when distant and 0ms only when within interaction range.",
                        })
                    in_loop = False

            # -------------------------------------------------------------
            # Correctness Rule BUG001: Missing cb() in RegisterNUICallback
            # -------------------------------------------------------------
            if "registernuicallback(" in line_lower:
                in_nui_callback = True
                nui_callback_line = line_no
                nui_has_cb = False

            if in_nui_callback:
                if re.search(r"\bcb\s*\(", line):
                    nui_has_cb = True
                if line == "end" or line.startswith("end)"):
                    if not nui_has_cb:
                        issues.append({
                            "code": "BUG001",
                            "severity": "error",
                            "line": nui_callback_line,
                            "message": "RegisterNUICallback handler is missing callback completion 'cb()'.",
                            "recommendation": "Always invoke cb({ ok = true }) or cb('ok') to prevent client NUI fetch promises from hanging.",
                        })
                    in_nui_callback = False

            # -------------------------------------------------------------
            # Correctness Rule BUG003: APISet Environment Mismatch
            # -------------------------------------------------------------
            if env == "client":
                for s_native in _KNOWN_SERVER_ONLY_NATIVES:
                    if re.search(rf"\b{s_native}\b", line_lower):
                        issues.append({
                            "code": "BUG003",
                            "severity": "error",
                            "line": line_no,
                            "message": f"Server-only native '{s_native}' called in client script.",
                            "recommendation": "Move this call to a server script or invoke via TriggerServerEvent.",
                        })
            elif env == "server":
                for c_native in _KNOWN_CLIENT_ONLY_NATIVES:
                    if re.search(rf"\b{c_native}\b", line_lower):
                        issues.append({
                            "code": "BUG003",
                            "severity": "error",
                            "line": line_no,
                            "message": f"Client-only native '{c_native}' called in server script.",
                            "recommendation": "Move this call to a client script or invoke via TriggerClientEvent.",
                        })

        error_count = sum(1 for i in issues if i["severity"] == "error")
        warning_count = sum(1 for i in issues if i["severity"] == "warning")
        info_count = sum(1 for i in issues if i["severity"] == "info")

        is_valid = error_count == 0
        summary_parts = []
        if error_count > 0:
            summary_parts.append(f"{error_count} error{'s' if error_count > 1 else ''}")
        if warning_count > 0:
            summary_parts.append(f"{warning_count} warning{'s' if warning_count > 1 else ''}")
        if info_count > 0:
            summary_parts.append(f"{info_count} suggestion{'s' if info_count > 1 else ''}")

        summary = f"Audit passed with 0 issues." if not summary_parts else f"Found {', '.join(summary_parts)}."

        return {
            "valid": is_valid,
            "detected_environment": env,
            "summary": summary,
            "issues_count": len(issues),
            "issues": issues,
        }


# Global validator singleton instance
script_validator = ScriptValidator()
