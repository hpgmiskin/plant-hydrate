import os
import asyncio

import aioserial
import serial.tools.list_ports

def find_serial_port() -> str: 
    for port in serial.tools.list_ports.comports():
        if port.manufacturer:
            return port.device
    raise RuntimeError("No devices found")

async def read_and_print(aioserial_instance: aioserial.AioSerial):
    while True:
        raw_bytes = await aioserial_instance.read_async()
        string_message = raw_bytes.decode(errors='ignore')
        print(string_message, end='', flush=True)


port = find_serial_port()
aioserial_instance = aioserial.AioSerial(port=port)
asyncio.run(read_and_print(aioserial_instance))