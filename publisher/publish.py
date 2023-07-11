from time import sleep

import paho.mqtt.client as mqtt

from publisher.logger import get_logger
from publisher.settings import BROKER_HOST, MAX_RETRIES

logger = get_logger()


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logger.info("Connection established successfully")
    else:
        logger.info(f"Bad connection, error code: {rc}")


def try_connect(client: mqtt.Client):
    connected = False
    retries = 0
    max_retries = int(MAX_RETRIES)
    while not connected and retries < max_retries:
        try:
            client.connect(BROKER_HOST)
            connected = True
        except Exception as e:
            logger.error("Error while connecting to broker, retrying.")
            logger.error(e)
            # Retry again in one second
            sleep(1)
            retries += 1
            continue
    if not connected:
        logger.error("Max retries reached, exiting.")


# def publish_session(client: mqtt.Client):
#     client.publish("/hamada/light", "ON")

client = mqtt.Client("publisher")
client.on_connect = on_connect
client.loop_start()
try_connect(client)
# wait to ensure connection is established
sleep(2)
