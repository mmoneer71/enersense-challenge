import platform

import psutil
from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorClient  # type: ignore

from api.db import get_db

health_router = APIRouter()


@health_router.get("/", include_in_schema=False)
@health_router.get("")
async def health(db: AsyncIOMotorClient = Depends(get_db)):
    try:
        # Check if the database is responsive
        await db.command("ping")
        db_status = "up"
    except Exception:
        db_status = "down"

    # Get system information
    system_info = {
        "system": platform.system(),
        "processor": platform.processor(),
        "architecture": platform.architecture(),
        "memory": psutil.virtual_memory()._asdict(),
        "disk": psutil.disk_usage("/")._asdict(),
    }

    return {"database": db_status, "system_info": system_info}
