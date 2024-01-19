from motor.motor_asyncio import AsyncIOMotorClient  # type: ignore

from utils.logger import get_logger
from utils.settings import MONGO_DB_PASSWORD, MONGO_DB_USERNAME

# How to make this better?
# Avoid global variables please!
# How do we change this into a class, initiate it and pass the handler?
# Classes >> Functions when there is state
# Favor context managers over writing code
db_client: AsyncIOMotorClient = None
DB_CONNECTION_STR = f"mongodb+srv://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWORD}@mongo-db-es-assignment.7ok8jpt.mongodb.net/"

logger = get_logger("api_db")


async def get_db() -> AsyncIOMotorClient:
    return db_client["assignment"]


async def connect_and_init_db():
    global db_client
    try:
        db_client = AsyncIOMotorClient(DB_CONNECTION_STR)
        logger.info("Connected to mongo.")
    except Exception as e:
        logger.exception(f"Could not connect to mongo: {e}")
        raise


async def close_db_connect():
    global db_client
    if db_client is None:
        logger.warning("Connection is None, nothing to close.")
        return
    db_client.close()
    db_client = None
    logger.info("Mongo connection closed.")
