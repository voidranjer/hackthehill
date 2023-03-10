import time
import asyncio
import websockets
import serial


URI = "ws://172.20.10.7:8765"

ser = serial.Serial('COM3', 9800, timeout=1)
time.sleep(2)


async def listen():
    async with websockets.connect(URI) as websocket:
        while True:
            res = await websocket.recv()
            print(f"> {res}")

            if res == "landfill":
                led1()
            elif res == "metal":
                led2()
            elif res == "plastic":
                led3()
            elif res == "cardboard":
                led4()
            elif res == "nothing":
                ledOff()

            await asyncio.sleep(0.5)


def led1():
    ledOff()
    ser.write(b'1')


def led2():
    ledOff()
    ser.write(b'2')


def led3():
    ledOff()
    ser.write(b'3')


def led4():
    ledOff()
    ser.write(b'4')


def ledOff():
    ser.write(b'5')


if __name__ == "__main__":
    asyncio.run(listen())
