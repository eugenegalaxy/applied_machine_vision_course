'''
Lecture 3
Topic: Median Filter
This script applies a Median Filter to the image.
Each pixel is replaced by the median value of its neighbors.
It is very effective at removing "Salt and Pepper" noise (random white/black dots) while preserving edges.
'''

import cv2
import numpy as np
from picamzero import Camera

# Initialize camera
cam = Camera()

print("Starting Median Filter script. Press 'q' to exit.")

# Kernel size (must be odd integer, e.g. 3, 5, 7)
ksize = 5

try:
    while True:
        # Capture frame
        frame = cam.pc2.capture_array()

        # FIX: Check if frame has 4 channels (RGBA/BGRA) and convert to 3 channels (BGR)
        if frame.shape[2] == 4:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)

        # Apply Median Blur
        # Note: ksize is a single integer here, not a tuple
        filtered = cv2.medianBlur(frame, ksize)

        # Stack images side-by-side
        combined = cv2.hconcat([frame, filtered])

        # Add text overlay
        cv2.putText(combined, f"Median Filter Kernel: {ksize}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display
        cv2.imshow("Left: Original | Right: Median Filter", combined)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cv2.destroyAllWindows()

