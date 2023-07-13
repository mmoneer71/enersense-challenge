from app.db import add_payload_to_db, __get_payload

def test_add_to_db():
    payload_dict = {
        "session_id": 999,
        "timestamp": 1689166951,
        "energy_delivered_in_kwh": 30,
        "duration_in_seconds": 45,
        "session_cost_in_cents": 70,
    }
    payload = str(payload_dict)
    add_payload_to_db(payload)
    p = __get_payload(999)
    assert p["session_id"] == 999
