'''
Lecture 3
Topic: Edge Detection (Canny)
This script detects edges in the image using the Canny algorithm.
It finds areas with strong intensity gradients.
'''

import cv2
import numpy as np
from picamzero import Camera

# Initialize camera
cam = Camera()

print("Starting Edge Detection script. Press 'q' to exit.")

# Canny thresholds
threshold1 = 100
threshold2 = 200

try:
    while True:
        # Capture frame
        frame = cam.pc2.capture_array()

        # FIX: Check if frame has 4 channels (RGBA/BGRA) and convert to 3 channels (BGR)
        if frame.shape[2] == 4:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)

        # Convert to grayscale (Canny works on single channel)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply Canny Edge Detection
        edges = cv2.Canny(gray, threshold1, threshold2)

        # Convert edges back to BGR to stack with original frame
        edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

        # Stack images side-by-side
        combined = cv2.hconcat([frame, edges_bgr])

        # Add text overlay
        cv2.putText(combined, f"Canny Thresholds: {threshold1}, {threshold2}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display
        cv2.imshow("Left: Original | Right: Canny Edges", combined)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cv2.destroyAllWindows()

