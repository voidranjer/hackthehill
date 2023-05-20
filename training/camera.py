import cv2

# Open the default camera
cap = cv2.VideoCapture(1)

# Define a counter for naming the image files
count = 0

# Start capturing and saving images every 1 second
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(50)

    shouldCapture = False
    if key == ord('z'):
        break
    elif key == ord(" "):
        shouldCapture = True

    # If frame is read correctly, save to file
    if ret:
        # Construct the filename with the current timestamp
        filename = f"images/image_{count}.jpg"

        # Save the frame as a JPEG image
        if shouldCapture:
            cv2.imwrite(filename, frame)
            count += 1

# Release the camera
cap.release()
