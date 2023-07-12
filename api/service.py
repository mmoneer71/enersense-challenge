from api.db import AsyncIOMotorClient
from utils.logger import get_logger

logger = get_logger("api_service")


async def get_all_readings(conn: AsyncIOMotorClient):
    logger.info("Retreiving all readings from db")
    readings = await conn["charger_payload"].find().to_list(1000)
    return readings
