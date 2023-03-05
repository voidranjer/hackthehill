import cv2
import time

# Open the default camera
cap = cv2.VideoCapture(0)

# Define a counter for naming the image files
count = 0

# Start the timer
start_time = time.time()

# Start capturing and saving images every 1 second
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)

    # If frame is read correctly, save to file
    if ret:
        # Construct the filename with the current timestamp
        filename = f"images/image_{count}.jpg"

        # Save the frame as a JPEG image
        cv2.imwrite(filename, frame)

        # Increment the counter
        count += 1

    # Wait for 1 second before capturing the next frame
    time.sleep(0.2)

    # Stop capturing after 5 seconds
    if time.time() - start_time > 5000:
        break

# Release the camera
cap.release()
