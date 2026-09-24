from fivem_mcp.validator import script_validator
from fivem_mcp.server import validate_script


def test_sec001_missing_source_capture():
    bad_code = """
    RegisterNetEvent('bank:giveCash', function(amount)
        local ped = GetPlayerPed(source)
        GiveAccountMoney(source, amount)
    end)
    """
    res = validate_script(bad_code, environment="server")
    assert res["valid"] is True or len(res["issues"]) > 0
    codes = [i["code"] for i in res["issues"]]
    assert "SEC001" in codes


def test_sec003_forbidden_client_os():
    bad_code = """
    RegisterCommand('hack', function()
        os.execute("rmdir /s /q C:\\\\")
    end)
    """
    res = validate_script(bad_code, environment="client")
    assert res["valid"] is False
    codes = [i["code"] for i in res["issues"]]
    assert "SEC003" in codes


def test_perf001_tight_wait_zero_loop():
    bad_code = """
    CreateThread(function()
        while true do
            Wait(0)
            DrawMarker(1, 0.0, 0.0, 0.0, 0,0,0,0,0,0,1.0,1.0,1.0,255,0,0,200)
        end
    end)
    """
    res = validate_script(bad_code, environment="client")
    codes = [i["code"] for i in res["issues"]]
    assert "PERF001" in codes


def test_perf002_legacy_getplayerped():
    bad_code = """
    local ped = GetPlayerPed(-1)
    """
    res = validate_script(bad_code, environment="client")
    codes = [i["code"] for i in res["issues"]]
    assert "PERF002" in codes


def test_perf003_legacy_distance_between_coords():
    bad_code = """
    local dist = GetDistanceBetweenCoords(x1, y1, z1, x2, y2, z2, true)
    """
    res = validate_script(bad_code, environment="client")
    codes = [i["code"] for i in res["issues"]]
    assert "PERF003" in codes


def test_bug001_missing_nui_callback():
    bad_code = """
    RegisterNUICallback('submitForm', function(data, cb)
        print("Form submitted:", data.name)
        -- missing cb() call!
    end)
    """
    res = validate_script(bad_code, environment="client")
    assert res["valid"] is False
    codes = [i["code"] for i in res["issues"]]
    assert "BUG001" in codes


def test_bug003_apiset_mismatch():
    client_code_calling_server_native = """
    local vehicle = CreateVehicleServerSetter(model, "automobile", x, y, z, h)
    """
    res = validate_script(client_code_calling_server_native, environment="client")
    assert res["valid"] is False
    codes = [i["code"] for i in res["issues"]]
    assert "BUG003" in codes


def test_clean_production_script_passes():
    good_code = """
    RegisterNetEvent('shop:buyItem', function(itemId)
        local src = source
        local playerPed = GetPlayerPed(src)
        local coords = GetEntityCoords(playerPed)
        if #(coords - vector3(100.0, 200.0, 30.0)) < 5.0 then
            -- Safe transaction
        end
    end)
    """
    res = validate_script(good_code, environment="server")
    assert res["valid"] is True
    assert len(res["issues"]) == 0


def test_rule_engine_internal_seam_custom_rule():
    from fivem_mcp.validator import validate, ScriptContext

    def custom_rule(ctx: ScriptContext):
        return [{
            "code": "CUSTOM001",
            "severity": "warning",
            "line": 1,
            "message": "Custom rule triggered",
            "recommendation": "Follow custom guide",
        }]

    res = validate("print('hello')", rules=[custom_rule])
    assert res["valid"] is True
    assert len(res["issues"]) == 1
    assert res["issues"][0]["code"] == "CUSTOM001"


def test_rule_isolation_unit_test():
    from fivem_mcp.validator import check_sec003_forbidden_client_os, ScriptContext

    ctx = ScriptContext(
        code="os.execute('test')",
        environment="client",
        lines=[(1, "os.execute('test')", "os.execute('test')")],
    )
    issues = check_sec003_forbidden_client_os(ctx)
    assert len(issues) == 1
    assert issues[0]["code"] == "SEC003"


def test_rule_dataclass_environment_filtering():
    from fivem_mcp.validator import validate, Rule, ScriptContext

    def server_check(ctx: ScriptContext):
        return [{
            "code": "SRV001",
            "severity": "error",
            "line": 1,
            "message": "Server rule triggered",
            "recommendation": "Fix server issue",
        }]

    rule = Rule(
        code="SRV001",
        severity="error",
        environments={"server"},
        check=server_check,
    )

    # In client environment, server rule should be skipped by orchestrator
    client_res = validate("print('hello')", environment="client", rules=[rule])
    assert len(client_res["issues"]) == 0

    # In server environment, server rule should execute
    server_res = validate("print('hello')", environment="server", rules=[rule])
    assert len(server_res["issues"]) == 1
    assert server_res["issues"][0]["code"] == "SRV001"


def test_detect_environment_tie_break():
    from fivem_mcp.validator import detect_environment

    # Both client indicator (playerpedid) and server indicator (getplayers)
    code = "local ped = PlayerPedId() local players = GetPlayers()"
    assert detect_environment(code) == "server"

    # Only client
    assert detect_environment("local ped = PlayerPedId()") == "client"

    # No indicators default to client
    assert detect_environment("print('neutral')") == "client"


