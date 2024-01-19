from app.db import AsyncIOMotorClient
from utils.logger import get_logger

logger = get_logger("api_service")

# if you don't know, favor async
# if you know what you're doing don't use async
# if you are sure what you are doing, feel free to choose yourself
async def get_all_readings(conn: AsyncIOMotorClient):
    logger.info("Retreiving all readings from db")
    readings = await conn["charger_payload"].find().to_list(1000)
    return readings
