import cv2
import numpy as np

# Define a function to detect the gesture
def detect_gesture(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Blur the image to reduce noise
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Threshold the image to create a binary image
    _, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    
    # Find contours in the binary image
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # If there are contours, find the largest one and use its shape to detect the gesture
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        if cv2.contourArea(c) > 1000:
            gesture = ""
            hull = cv2.convexHull(c)
            defects = cv2.convexityDefects(c, hull)
            if defects is not None:
                for i in range(defects.shape[0]):
                    s, e, f, d = defects[i, 0]
                    start = tuple(c[s][0])
                    end = tuple(c[e][0])
                    far = tuple(c[f][0])
                    if d > 10000:
                        gesture = "Hand Open"
                    else:
                        gesture = "Hand Closed"
            return gesture
    return ""

# Capture video from the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    
    # Detect the gesture
    gesture = detect_gesture(frame)
    
    # Display the gesture on the frame
    cv2.putText(frame, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
    
    # Show the frame
    cv2.imshow("Gesture Recognition", frame)
    
    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture
cap.release()

# Destroy all windows
cv2.destroyAllWindows()
