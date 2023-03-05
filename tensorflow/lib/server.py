from tensorflow_model import TFModel
from PIL import Image
import os
import cv2
import asyncio
import websockets

# printing only warnings and error messages
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "1"

# Store all connected clients in a set
connected_clients = set()


async def handle_client(websocket, path):
    # Add the client to the set of connected clients
    connected_clients.add(websocket)
    print(
        f"Client connected, {len(connected_clients)} client(s) currently connected")
    try:
        # Handle incoming messages from the client
        async for message in websocket:
            print(f"Received message from client: {message}")
    finally:
        # Remove the client from the set of connected clients when they disconnect
        connected_clients.remove(websocket)
        print(
            f"Client disconnected, {len(connected_clients)} client(s) currently connected")


async def send_message(message):
    # Send a message to all connected clients
    for client in connected_clients:
        await client.send(message)
    print(f"Sent message to {len(connected_clients)} client(s): {message}")


async def main():
    # Load TensorFlow model
    dir_path = os.getcwd()
    model = TFModel(dir_path=dir_path)

    # Set up the WebSocket server
    async with websockets.serve(handle_client, "localhost", 8765):
        print("WebSocket server started")

        # Capture webcam footage
        key = cv2. waitKey(1)
        webcam = cv2.VideoCapture(0)

        prev_highest_confidence = None
        while True:
            try:
                check, frame = webcam.read()
                # print(check) #prints true as long as the webcam is running
                # print(frame) #prints matrix values of each framecd
                cv2.imshow("Capturing", frame)
                key = cv2.waitKey(1)

                # break
                if key == ord('q'):
                    webcam.release()
                    cv2.destroyAllWindows()
                    break

            except(KeyboardInterrupt):
                webcam.release()
                cv2.destroyAllWindows()
                break

            image = Image.fromarray(frame)
            results = model.predict(image)
            highest_confidence = results["predictions"][0]["label"]

            # Send a message to the client if the highest confidence has changed
            if highest_confidence != prev_highest_confidence:
                await send_message(highest_confidence)

            prev_highest_confidence = highest_confidence


if __name__ == "__main__":
    asyncio.run(main())
