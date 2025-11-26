'''
Lecture 2
Topic: Grayscale Conversion
This script captures the live feed from the camera, converts it to grayscale,
and displays the original and grayscale versions side-by-side.
'''

import cv2
import numpy as np
from picamzero import Camera

# Initialize camera
cam = Camera()

print("Starting Grayscale script. Press 'q' to exit.")

try:
    while True:
        # Capture frame as numpy array using underlying Picamera2 instance
        frame = cam.pc2.capture_array()

        # FIX: Check if frame has 4 channels (RGBA/BGRA) and convert to 3 channels (BGR)
        if frame.shape[2] == 4:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)

        # Convert to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Convert grayscale back to BGR so we can stack it with the original color frame
        gray_bgr = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)

        # Stack images side-by-side
        combined = cv2.hconcat([frame, gray_bgr])

        # Display
        cv2.imshow("Left: Original | Right: Grayscale", combined)

        # Check for 'q' key to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cv2.destroyAllWindows()
    cam.stop_preview() # Good practice to ensure resources are released

