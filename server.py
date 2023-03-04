import asyncio
import websockets


async def send(websocket):
    await websocket.send("Hello world! That is perfect")
    # async for message in websocket:
    # await websocket.send(message)


async def main():
    async with websockets.serve(send, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
