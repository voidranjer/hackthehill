import asyncio
import websockets
from playsound import playsound


URI = "ws://172.20.10.7:8765"


async def listen():
    async with websockets.connect(URI) as websocket:
        while True:
            res = await websocket.recv()
            print(f"> {res}")

            if res == "landfill":
                play_file("sound/first.mp3")
            elif res == "metal":
                play_file("sound/second.mp3")
            elif res == "plastic":
                play_file("sound/third.mp3")
            elif res == "cardboard":
                play_file("sound/fourth.mp3")

            await asyncio.sleep(0.5)


# function to play a file
def play_file(file):
    playsound(file)


if __name__ == "__main__":
    asyncio.run(listen())
