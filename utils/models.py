from uuid import UUID

from pydantic import BaseModel


class MongoModel(BaseModel):
    @classmethod
    def from_mongo(cls, data: dict):
        if not data:
            return data
        id = data.pop("_id", None)
        return cls(**dict(data, id=id))

    def mongo(self, **kwargs):
        exclude_unset = kwargs.pop("exclude_unset", True)
        by_alias = kwargs.pop("by_alias", True)
        parsed = self.model_dump(
            exclude_unset=exclude_unset,
            by_alias=by_alias,
            **kwargs,
        )

        if "_id" not in parsed and "id" in parsed:
            parsed["_id"] = parsed.pop("id")

        return parsed


class ChargerPayload(BaseModel):
    session_id: int
    timestamp: int
    energy_delivered_in_kwh: int
    duration_in_seconds: int
    session_cost_in_cents: int


class DbChargerPayload(MongoModel):
    session_id: int
    timestamp: int
    energy_delivered_in_kwh: int
    duration_in_seconds: int
    session_cost_in_cents: int
