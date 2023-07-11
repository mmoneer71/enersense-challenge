from pydantic import BaseModel


class ChargerPayload(BaseModel):
    session_id: int
    timestamp: int
    energy_delivered_in_kwh: int
    duration_in_seconds: int
    session_cost_in_cents: int
