from time import sleep

import paho.mqtt.client as mqtt

from utils.logger import get_logger
from utils.settings import BROKER_HOST, BROKER_PORT, MAX_RETRIES

logger = get_logger()


class MqttClientWrapper:
    def __init__(
        self, client_id: str, host: str = BROKER_HOST, port: int = int(BROKER_PORT)
    ) -> None:
        self.mqtt_client = mqtt.Client(client_id)
        self.mqtt_client.on_connect = MqttClientWrapper.on_connect

        self.host = host
        self.port = port

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            logger.info("Connection established successfully")
        else:
            logger.info(f"Bad connection, error code: {rc}")
    
    def try_connect(self):
        success = False
        retries = 0
        max_retries = int(MAX_RETRIES)
        while not success and retries < max_retries:
            try:
                self.mqtt_client.connect(self.host, self.port)
                self.mqtt_client.loop_start()
                success = True
            except Exception as e:
                logger.error("Error while connecting to broker, retrying.")
                logger.error(e)
                # Retry again in one second
                sleep(1)
                retries += 1
                continue
        if not success:
            logger.error("Max retries reached, exiting.")
