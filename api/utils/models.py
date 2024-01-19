from uuid import UUID

from pydantic import BaseModel

# bad idea for bigger applications
# please create router/service/model combo whenever contextually appropriate!
# this file is for main level models YET,
# please don't create too many many layers either. "Calibrate son :D"
# also, please name the root level dir something that relates to the project
# not api, not src, not app, nothing TOO general
# please ignore MongoModel, it's a piece of crap for the assignment
# example naming: enersense-challenge for bitbucket name
# example root dir name: enersense_challenge
# also api spec generation is missing, must be added might be a good idea to
# be a pre-commit. Also check if there are unintended changes in
# pre-commit hooks in UPAPI.

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

# for example, these shouldn't live in the main level models
# but shitty MongoModel can

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
