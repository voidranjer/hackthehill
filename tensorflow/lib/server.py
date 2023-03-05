import os
import cv2
from PIL import Image
import asyncio
from tensorflow_model import TFModel

# printing only warnings and error messages
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "1"

async def main():
    # Load model
    dir_path = os.getcwd()
    model = TFModel(dir_path=dir_path)

    # Capture webcam footage
    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)
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


if __name__ == "__main__":
    asyncio.run(main())
