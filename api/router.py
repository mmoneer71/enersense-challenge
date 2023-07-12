from typing import List

from fastapi import APIRouter, Depends

import api.service as service
from api.db import AsyncIOMotorClient, get_db
from api.samples import sample_ev_readings
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
    db: AsyncIOMotorClient = Depends(get_db),
) -> List[ChargerPayload]:
    readings = await service.get_all_readings(db)
    return readings
