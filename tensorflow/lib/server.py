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
HOST = "0.0.0.0"
CONNECTIONS = set()

CONFIDENCE_THRESH = 0.8
BUFFER_SIZE = 15


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
    webcam = cv2.VideoCapture(0)

    prev_highest_label = None

    # Buffer queue
    buffer_queue = [None for i in range(BUFFER_SIZE)]
    counter = 0

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
        most_confident_result = results["predictions"][0]

        print(most_confident_result)
        highest_label = most_confident_result["label"]
        highest_confidence = most_confident_result["confidence"]

        if (counter < BUFFER_SIZE):
            buffer_queue[counter] = highest_label
            counter += 1
        else:
            counter = 0
            buffer_queue[0] = highest_label

            current_highest_label = max(buffer_queue,key=buffer_queue.count)

            # Send a message to the client if the highest confidence has changed (and is above threshold)
            if (current_highest_label != prev_highest_label and highest_confidence > CONFIDENCE_THRESH):
            # if (current_highest_label != prev_highest_label and highest_confidence > CONFIDENCE_THRESH):
                websockets.broadcast(CONNECTIONS, current_highest_label)
                print(
                    f"Sent message to {len(CONNECTIONS)} clients: {current_highest_label}")

            prev_highest_label = current_highest_label
        # Delay required otherwise websocket server will not receive connections
        await asyncio.sleep(0.01)


async def test_server():
    while True:
        websockets.broadcast(CONNECTIONS, "popcorners")
        print("Broadcasting...")
        await asyncio.sleep(1)


async def main():
    async with websockets.serve(register, HOST, WEBSOCKETS_PORT):
        await tensorflow_detection()
        # await test_server()

if __name__ == "__main__":
    asyncio.run(main())
