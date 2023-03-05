import asyncio
import websockets


async def listen():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            res = await websocket.recv()
            print(f"<<< {res}")
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(listen())
