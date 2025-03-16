import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point, WritePrecision
import json
import os

# MQTT Broker Configuration
MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_TOPIC = "sensor/data"

# InfluxDB Configuration for Time-Series Data
INFLUXDB_URL = os.getenv("INFLUXDB_URL", "http://localhost:8086")
INFLUXDB_TOKEN = os.getenv("INFLUXDB_TOKEN", "your-influxdb-token")
INFLUXDB_ORG = os.getenv("INFLUXDB_ORG", "sims_org")
INFLUXDB_BUCKET = os.getenv("INFLUXDB_BUCKET", "sensor_data")

influx_client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)
influx_write_api = influx_client.write_api(write_options=WritePrecision.NS)

# MQTT Client Setup
def on_connect(client, userdata, flags, rc):
    """Handle connection to MQTT broker."""
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(MQTT_TOPIC)
    else:
        print("Failed to connect, return code ", rc)

def on_message(client, userdata, msg):
    """Process incoming MQTT messages and store sensor data."""
    try:
        payload = json.loads(msg.payload.decode('utf-8'))
        sensor_id = payload.get("sensor_id")
        value = payload.get("value")
        timestamp = payload.get("timestamp")
        
        # Store in InfluxDB
        point = Point("sensor_data").tag("sensor_id", sensor_id).field("value", value).time(timestamp, WritePrecision.NS)
        influx_write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=point)
        
        print("Sensor data saved to InfluxDB:", payload)
    except Exception as e:
        print("Error processing MQTT message:", e)

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
mqtt_client.loop_start()