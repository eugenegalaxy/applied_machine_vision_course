'''
Lecture 3
Topic: Mean Filter (Box Blur / Averaging)
This script applies a Mean (Average) Filter to the image.
Each pixel is replaced by the average value of its neighbors.
'''

import cv2
import numpy as np
from picamzero import Camera

# Initialize camera
cam = Camera()

print("Starting Mean Filter script. Press 'q' to exit.")

# Kernel size
ksize = (5, 5)

try:
    while True:
        # Capture frame
        frame = cam.pc2.capture_array()

        # FIX: Check if frame has 4 channels (RGBA/BGRA) and convert to 3 channels (BGR)
        if frame.shape[2] == 4:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)

        # Apply Mean Filter (cv2.blur)
        blurred = cv2.blur(frame, ksize)

        # Stack images side-by-side
        combined = cv2.hconcat([frame, blurred])

        # Add text overlay
        cv2.putText(combined, f"Mean Filter Kernel: {ksize}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display
        cv2.imshow("Left: Original | Right: Mean Filter", combined)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cv2.destroyAllWindows()

