from random import randint
from time import sleep
from typing import Dict

import pendulum as pdl

from utils.connect import MqttClientWrapper
from utils.logger import get_logger
from utils.models import ChargerPayload
from utils.settings import MQTT_TOPIC_BASE

logger = get_logger("publisher")


def on_publish(client, userdata, result):  # create function for callback
    logger.info("Data published successfully")


def generate_session_payload(session_id: int) -> ChargerPayload:
    new_payload: Dict[str, int] = {}
    energy_kwh = randint(1, 100)

    new_payload["session_id"] = session_id
    new_payload["timestamp"] = pdl.now().utcnow().int_timestamp
    new_payload["energy_delivered_in_kwh"] = energy_kwh
    new_payload["duration_in_seconds"] = int(energy_kwh * 1.5)
    new_payload["session_cost_in_cents"] = int(energy_kwh * 2.5)
    return ChargerPayload(**new_payload)


def main():
    session_id = 1
    latest_timestamp = 0
    pub_mqtt_client = MqttClientWrapper(client_id="publisher")
    pub_mqtt_client.try_connect()
    # wait a few seconds to ensure connection
    sleep(2)
    pub_mqtt_client.mqtt_client.on_publish = on_publish
    while True:
        try:
            now = pdl.now().utcnow().int_timestamp
            if now - latest_timestamp < 60:
                continue
            session_topic = f"{MQTT_TOPIC_BASE}/{session_id}"
            payload = generate_session_payload(session_id)
            latest_timestamp = payload.timestamp
            logger.info(f"Publishing session {session_id}")
            pub_mqtt_client.mqtt_client.publish(
                topic=session_topic, payload=payload.model_dump_json(), qos=1
            )
        except Exception as e:
            logger.error(f"Error occurred while publishing session {session_id}")
            logger.error(e)
        session_id += 1
        sleep(10)


main()
