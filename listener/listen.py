import signal
import sys
from time import sleep

import pendulum as pdl

from listener.db import add_payload_to_db
from utils.connect import MqttClientWrapper
from utils.logger import get_logger
from utils.settings import MQTT_TOPIC_BASE

logger = get_logger("listener")
sub_mqtt_client = MqttClientWrapper(client_id="listener")


def keyboard_interrupt_handler(sig, frame):
    logger.info("Application terminated by keyboard interrupt")
    logger.info("Unsubscribing")
    sub_mqtt_client.mqtt_client.unsubscribe(topic=f"{MQTT_TOPIC_BASE}/#")
    logger.info("Disconnecting")
    sub_mqtt_client.mqtt_client.disconnect()
    # wait for ack
    sleep(1)
    sys.exit(0)


def on_subscribe(client, userdata, mid, granted_qos):
    logger.info(f"Subscribed successfully")


def on_unsubscribe(client, userdata, mid, granted_qos):
    logger.info(f"Unsubscribed successfully")


def on_message(client, userdata, message):
    payload = message.payload.decode("UTF-8")
    now = pdl.now().utcnow().int_timestamp
    logger.info(
        f"Received message {payload}"
        f" on topic {message.topic}"
        f" with QoS {message.qos}"
        f" at timestamp {now}"
    )
    add_payload_to_db(payload)


def main():
    logger.info("Connecting to mqtt broker")
    sub_mqtt_client.try_connect()
    # wait a few seconds to ensure connection
    sleep(2)
    sub_mqtt_client.mqtt_client.on_subscribe = on_subscribe
    sub_mqtt_client.mqtt_client.on_unsubscribe = on_unsubscribe
    sub_mqtt_client.mqtt_client.on_message = on_message
    signal.signal(signal.SIGINT, keyboard_interrupt_handler)
    logger.info(f"Subscribing to wild-card topic {MQTT_TOPIC_BASE}/#")
    sub_mqtt_client.mqtt_client.subscribe(topic=f"{MQTT_TOPIC_BASE}/#", qos=1)
    # ugly way because loop_forever() was crashing
    while True:
        sleep(1)


main()
