import asyncio
import logging
import os

import aioserial
import dotenv
import serial.tools.list_ports

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import ASYNCHRONOUS

dotenv.load_dotenv()

BALENA_DEVICE_NAME = os.getenv("BALENA_DEVICE_NAME_AT_INIT", "testing")

INFLUX_URL = "https://eu-central-1-1.aws.cloud2.influxdata.com"
INFLUX_ORGANIZATION = os.getenv("INFLUX_ORGANIZATION")
INFLUX_BUCKET = os.getenv("INFLUX_BUCKET")
INFLUX_TOKEN = os.getenv("INFLUX_TOKEN")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

influx_client = InfluxDBClient(url=INFLUX_URL, org=INFLUX_ORGANIZATION, token=INFLUX_TOKEN)
influx_write_api = influx_client.write_api(write_options=ASYNCHRONOUS)

def find_serial_port() -> str: 
    for port in serial.tools.list_ports.comports():
        if port.manufacturer:
            return port.device
    raise RuntimeError("No devices found")

def write_influx_data(point:str, field:str, value:float):
    point = Point(point).tag("device-name", BALENA_DEVICE_NAME).field(field, value)
    influx_write_api.write(bucket=INFLUX_BUCKET, record=[point])

async def read_and_store(aioserial_instance: aioserial.AioSerial):
    while True:
        raw_bytes = await aioserial_instance.readline_async()
        string_message = raw_bytes.decode(errors='ignore')
        [name, value] = string_message.strip("\n\r").split(":")
        logger.info("read value %s = %s", name, value)
        write_influx_data("serial", name, float(value))
        

def main():
    port = find_serial_port()
    logger.info("found port %s", port)
    aioserial_instance = aioserial.AioSerial(port=port)
    asyncio.run(read_and_store(aioserial_instance))


if __name__ == "__main__":
    main()