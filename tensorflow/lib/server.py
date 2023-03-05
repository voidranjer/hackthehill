from tensorflow_model import TFModel
from PIL import Image
import os
import cv2
import asyncio
import websockets

# printing only warnings and error messages
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "1"

# Store all connected clients in a set
WEBSOCKETS_PORT = 8765
CONNECTIONS = set()


async def register(websocket):
    CONNECTIONS.add(websocket)
    print(
        f"Client connected, {len(CONNECTIONS)} client(s) currently connected")
    try:
        await websocket.wait_closed()
    finally:
        CONNECTIONS.remove(websocket)
        print(
            f"Client disconnected, {len(CONNECTIONS)} client(s) currently connected")


async def tensorflow_detection():
    # Load TensorFlow model
    dir_path = os.getcwd()
    model = TFModel(dir_path=dir_path)

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
            websockets.broadcast(CONNECTIONS, highest_confidence)
            print(
                f"Sent message to {len(CONNECTIONS)} clients: {highest_confidence}")

        prev_highest_confidence = highest_confidence
        # Delay required otherwise websocket server will not receive connections
        await asyncio.sleep(2)


async def main():
    async with websockets.serve(register, "localhost", WEBSOCKETS_PORT):
        await tensorflow_detection()

if __name__ == "__main__":
    asyncio.run(main())
