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
