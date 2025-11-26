'''
Lecture 3
Topic: Image Blur (Gaussian Blur)
This script applies a Gaussian Blur to the live video feed.
Blurring is often used to reduce noise or detail in an image.
'''

import cv2
import numpy as np
from picamzero import Camera

# Initialize camera
cam = Camera()

print("Starting Image Blur script. Press 'q' to exit.")

# Kernel size (must be odd numbers, e.g. (3,3), (5,5), (15,15))
ksize = (15, 15)

try:
    while True:
        # Capture frame
        frame = cam.pc2.capture_array()

        # FIX: Check if frame has 4 channels (RGBA/BGRA) and convert to 3 channels (BGR)
        if frame.shape[2] == 4:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)

        # Apply Gaussian Blur
        # sigmaX=0 means standard deviation is calculated from kernel size
        blurred = cv2.GaussianBlur(frame, ksize, 0)

        # Stack images side-by-side
        combined = cv2.hconcat([frame, blurred])

        # Add text overlay
        cv2.putText(combined, f"Kernel: {ksize}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display
        cv2.imshow("Left: Original | Right: Gaussian Blur", combined)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cv2.destroyAllWindows()

