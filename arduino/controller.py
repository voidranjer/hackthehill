import time
#import vlc
import asyncio
import websockets
import serial
from playsound import playsound


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
    play_file("first.mp3")


def led2():
    ledOff()
    ser.write(b'2')
    play_file("second.mp3")


def led3():
    ledOff()
    ser.write(b'3')
    play_file("third.mp3")


def led4():
    ledOff()
    ser.write(b'4')
    play_file("fourth.mp3")


def ledOff():
    ser.write(b'5')

# function to play a file


def play_file(file):
    # print("Playing")
    playsound(file)
    # print("Done")


# for i in range(2):
#     led1()
#     time.sleep(4)
#     led2()
#     time.sleep(4)
#     led3()
#     time.sleep(4)


if __name__ == "__main__":
    asyncio.run(listen())
