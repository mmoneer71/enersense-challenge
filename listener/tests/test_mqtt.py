from utils.connect import MqttClientWrapper

def test_try_connect():
    # Checking no exceptions occur
    c = MqttClientWrapper("test")
    c.try_connect()
    c.mqtt_client.disconnect()