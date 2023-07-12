from ast import literal_eval
from typing import Optional

from pydantic import ValidationError
from pymongo import MongoClient

from utils.logger import get_logger
from utils.models import DbChargerPayload
from utils.settings import MONGO_DB_PASSWORD, MONGO_DB_USERNAME

DB_CONNECTION_STR = f"mongodb+srv://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWORD}@mongo-db-es-assignment.7ok8jpt.mongodb.net/"
db_client: MongoClient = MongoClient(DB_CONNECTION_STR)
db_name = db_client["assignment"]
collection = db_name["charger_payload"]
logger = get_logger("listener_db")


def add_payload_to_db(payload: str) -> Optional[DbChargerPayload]:
    try:
        payload_dict = literal_eval(payload)
        new_payload = DbChargerPayload(**payload_dict)
        collection.insert_one(new_payload.mongo())
        logger.info("Payload added to database succcessfully")
        return new_payload
    except ValidationError:
        logger.error("Failed to parse data, missing keys or corrupt payload")
        return None


def close_connection():
    db_client.close()
