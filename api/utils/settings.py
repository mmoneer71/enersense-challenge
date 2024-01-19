import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

# ditch this and do it the data-api way aka pydantic settings
MONGO_DB_USERNAME = os.getenv("MONGO_DB_USERNAME", "enersense-assignment")
MONGO_DB_PASSWORD = os.getenv("MONGO_DB_PASSWORD", "")
