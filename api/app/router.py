from typing import List

from fastapi import APIRouter, Depends

import app.service as service
from app.db import AsyncIOMotorClient, get_db
from app.samples import sample_ev_readings
from utils.models import ChargerPayload

api_router = APIRouter()


@api_router.get(
    "/",
    tags=["readings"],
    responses={
        200: {
            "model": ChargerPayload,
            "description": "Get all EV readings",
            "content": {"application/json": {"example": sample_ev_readings}},
        },
        204: {},
    },
)
async def get_all_readings(
    # if we change our db.py to a class, we can
    # do this differently and better/can maintain
    # sessions/connections easier
    # perhaps follow the idea behind data-api?
    # it is already clean and we can just use it
    db: AsyncIOMotorClient = Depends(get_db),
) -> List[ChargerPayload]:
    readings = await service.get_all_readings(db)
    return readings
