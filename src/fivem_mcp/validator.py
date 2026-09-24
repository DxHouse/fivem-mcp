import re
from dataclasses import dataclass
from typing import Any, Callable

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


@dataclass(slots=True)
class ScriptContext:
    """Pre-parsed Lua script representation passed to rule predicates."""
    code: str
    environment: str
    lines: list[tuple[int, str, str]]  # (line_no, raw_line, lower_stripped_line)


def detect_environment(code: str) -> str:
    """Infer execution environment (client, server, or shared) based on heuristics."""
    code_lower = code.lower()
    server_hits = sum(1 for kw in _SERVER_INDICATORS if kw in code_lower)
    client_hits = sum(1 for kw in _CLIENT_INDICATORS if kw in code_lower)
    return "server" if server_hits > client_hits else "client"


# ============================================================================
# Individual Rule Predicates (Internal Seam)
# ============================================================================

def check_sec003_forbidden_client_os(ctx: ScriptContext) -> list[dict[str, Any]]:
    """SEC003: Detect forbidden operating system and file IO calls in client scripts."""
    if ctx.environment not in ("client", "auto"):
        return []
    issues = []
    for line_no, _, line_lower in ctx.lines:
        for forbidden, reason in _FORBIDDEN_CLIENT_FUNCS.items():
            if forbidden in line_lower:
                issues.append({
                    "code": "SEC003",
                    "severity": "error",
                    "line": line_no,
                    "message": f"Forbidden OS library call '{forbidden}' in client environment.",
                    "recommendation": reason,
                })
    return issues


def check_sec001_missing_source_capture(ctx: ScriptContext) -> list[dict[str, Any]]:
    """SEC001: Detect uncaptured global 'source' across server event handlers."""
    if ctx.environment not in ("server", "auto"):
        return []
    issues = []
    in_event = False
    event_line = 0
    has_src = False
    used_source = False

    for line_no, raw_line, line_lower in ctx.lines:
        if "registernetevent(" in line_lower or "registerserverevent(" in line_lower:
            in_event = True
            event_line = line_no
            has_src = False
            used_source = False

        if in_event:
            if re.search(r"local\s+([a-zA-Z0-9_]+)\s*=\s*source\b", raw_line):
                has_src = True
            elif re.search(r"\bsource\b", raw_line):
                used_source = True

            if line_lower == "end" or line_lower.startswith("end)"):
                if not has_src and used_source:
                    issues.append({
                        "code": "SEC001",
                        "severity": "warning",
                        "line": event_line,
                        "message": "Server event handler uses global 'source' without immediate local capture.",
                        "recommendation": "Capture 'local src = source' at the very beginning of the event handler closure.",
                    })
                in_event = False

    return issues


def check_perf002_legacy_player_ped(ctx: ScriptContext) -> list[dict[str, Any]]:
    """PERF002: Detect calls to legacy GetPlayerPed(-1)."""
    issues = []
    for line_no, _, line_lower in ctx.lines:
        if "getplayerped(-1)" in line_lower:
            issues.append({
                "code": "PERF002",
                "severity": "warning",
                "line": line_no,
                "message": "Use of legacy 'GetPlayerPed(-1)'.",
                "recommendation": "Replace with modern 'PlayerPedId()' or cache entity handle once outside loop.",
            })
    return issues


def check_perf003_legacy_distance(ctx: ScriptContext) -> list[dict[str, Any]]:
    """PERF003: Detect legacy GetDistanceBetweenCoords calls."""
    issues = []
    for line_no, _, line_lower in ctx.lines:
        if "getdistancebetweencoords(" in line_lower:
            issues.append({
                "code": "PERF003",
                "severity": "info",
                "line": line_no,
                "message": "Use of legacy 'GetDistanceBetweenCoords'.",
                "recommendation": "Replace with native vector arithmetic and length operator: '#(posA - posB)'.",
            })
    return issues


def check_perf001_tight_wait_loop(ctx: ScriptContext) -> list[dict[str, Any]]:
    """PERF001: Detect tight while true do Wait(0) loops lacking distance or sleep logic."""
    issues = []
    in_loop = False
    loop_line = 0
    has_wait_zero = False
    has_distance = False

    for line_no, _, line_lower in ctx.lines:
        if re.search(r"while\s+true\s+do", line_lower):
            in_loop = True
            loop_line = line_no
            has_wait_zero = False
            has_distance = False

        if in_loop:
            if re.search(r"(citizen\.)?wait\(\s*0\s*\)", line_lower):
                has_wait_zero = True
            if "distance" in line_lower or "#(" in line_lower or "sleep" in line_lower:
                has_distance = True

            if line_lower == "end" or line_lower.startswith("end)"):
                if has_wait_zero and not has_distance:
                    issues.append({
                        "code": "PERF001",
                        "severity": "warning",
                        "line": loop_line,
                        "message": "Tight 'while true do Wait(0)' loop without dynamic sleep or distance check.",
                        "recommendation": "Use dynamic wait: set sleep interval (e.g. 1000ms) when distant and 0ms only when within interaction range.",
                    })
                in_loop = False

    return issues


def check_bug001_missing_nui_cb(ctx: ScriptContext) -> list[dict[str, Any]]:
    """BUG001: Detect missing cb() callback invocation in RegisterNUICallback."""
    issues = []
    in_nui = False
    nui_line = 0
    has_cb = False

    for line_no, raw_line, line_lower in ctx.lines:
        if "registernuicallback(" in line_lower:
            in_nui = True
            nui_line = line_no
            has_cb = False

        if in_nui:
            if re.search(r"\bcb\s*\(", raw_line):
                has_cb = True

            if line_lower == "end" or line_lower.startswith("end)"):
                if not has_cb:
                    issues.append({
                        "code": "BUG001",
                        "severity": "error",
                        "line": nui_line,
                        "message": "RegisterNUICallback handler is missing callback completion 'cb()'.",
                        "recommendation": "Always invoke cb({ ok = true }) or cb('ok') to prevent client NUI fetch promises from hanging.",
                    })
                in_nui = False

    return issues


def check_bug003_apiset_mismatch(ctx: ScriptContext) -> list[dict[str, Any]]:
    """BUG003: Detect client-only natives in server code or server-only natives in client code."""
    issues = []
    if ctx.environment == "client":
        for line_no, _, line_lower in ctx.lines:
            for s_native in _KNOWN_SERVER_ONLY_NATIVES:
                if re.search(rf"\b{s_native}\b", line_lower):
                    issues.append({
                        "code": "BUG003",
                        "severity": "error",
                        "line": line_no,
                        "message": f"Server-only native '{s_native}' called in client script.",
                        "recommendation": "Move this call to a server script or invoke via TriggerServerEvent.",
                    })
    elif ctx.environment == "server":
        for line_no, _, line_lower in ctx.lines:
            for c_native in _KNOWN_CLIENT_ONLY_NATIVES:
                if re.search(rf"\b{c_native}\b", line_lower):
                    issues.append({
                        "code": "BUG003",
                        "severity": "error",
                        "line": line_no,
                        "message": f"Client-only native '{c_native}' called in server script.",
                        "recommendation": "Move this call to a client script or invoke via TriggerClientEvent.",
                    })
    return issues


DEFAULT_RULES: list[Callable[[ScriptContext], list[dict[str, Any]]]] = [
    check_sec003_forbidden_client_os,
    check_sec001_missing_source_capture,
    check_perf002_legacy_player_ped,
    check_perf003_legacy_distance,
    check_perf001_tight_wait_loop,
    check_bug001_missing_nui_cb,
    check_bug003_apiset_mismatch,
]


# ============================================================================
# Engine Orchestration
# ============================================================================

def validate(
    code: str,
    environment: str = "auto",
    rules: list[Callable[[ScriptContext], list[dict[str, Any]]]] | None = None,
) -> dict[str, Any]:
    """Perform static analysis on a FiveM Lua script and return structured diagnostics."""
    env = detect_environment(code) if environment == "auto" else environment.lower()
    active_rules = rules if rules is not None else DEFAULT_RULES

    # Pre-parse lines once for all rules
    parsed_lines = [
        (line_no, raw_line, raw_line.strip().lower())
        for line_no, raw_line in enumerate(code.splitlines(), start=1)
        if raw_line.strip() and not raw_line.strip().startswith("--")
    ]
    ctx = ScriptContext(code=code, environment=env, lines=parsed_lines)

    issues: list[dict[str, Any]] = []
    for rule_fn in active_rules:
        issues.extend(rule_fn(ctx))

    issues.sort(key=lambda x: x["line"])

    error_count = sum(1 for i in issues if i["severity"] == "error")
    warning_count = sum(1 for i in issues if i["severity"] == "warning")
    info_count = sum(1 for i in issues if i["severity"] == "info")

    summary_parts = []
    if error_count > 0:
        summary_parts.append(f"{error_count} error{'s' if error_count > 1 else ''}")
    if warning_count > 0:
        summary_parts.append(f"{warning_count} warning{'s' if warning_count > 1 else ''}")
    if info_count > 0:
        summary_parts.append(f"{info_count} suggestion{'s' if info_count > 1 else ''}")

    summary = "Audit passed with 0 issues." if not summary_parts else f"Found {', '.join(summary_parts)}."

    return {
        "valid": error_count == 0,
        "detected_environment": env,
        "summary": summary,
        "issues_count": len(issues),
        "issues": issues,
    }


class ScriptValidator:
    """Compatibility facade delegating to the modular rule engine."""

    detect_environment = staticmethod(detect_environment)

    @staticmethod
    def validate(
        code: str,
        environment: str = "auto",
        rules: list[Callable[[ScriptContext], list[dict[str, Any]]]] | None = None,
    ) -> dict[str, Any]:
        return validate(code, environment=environment, rules=rules)


# Global validator singleton instance
script_validator = ScriptValidator()
