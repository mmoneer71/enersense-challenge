import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

BROKER_HOST = os.getenv("BROKER_HOST", "broker.hivemq.com")
BROKER_PORT = os.getenv("BROKER_PORT", 1883)
MAX_RETRIES = os.getenv("MAX_RETRIES", 10)
MQTT_TOPIC_BASE = os.getenv("MQTT_TOPIC_BASE", "charger/1/connector/1/session")
