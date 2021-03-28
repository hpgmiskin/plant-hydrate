import aioserial
import asyncio

async def read_and_print(aioserial_instance: aioserial.AioSerial):
    while True:
        raw_bytes = await aioserial_instance.read_async()
        string_message = raw_bytes.decode(errors='ignore')
        print(string_message, end='', flush=True)

port = '/dev/cu.usbmodem63781901'
aioserial_instance = aioserial.AioSerial(port=port)
asyncio.run(read_and_print(aioserial_instance))