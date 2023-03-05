from PIL import Image
import time
import cv2
import os


# Initialize webcam
webcam = cv2.VideoCapture(0)

# Change the current directory to specified directory
directory = "/Users/meekranjer/Documents/git/hackthehill/training/images"
os.chdir(directory)

counter = 0

while True:
    counter += 1
    time.sleep(1)

    try:
        check, frame = webcam.read()
        print("Captured frame")

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
    cv2.imwrite(f"{counter}-training.jpg", image)
