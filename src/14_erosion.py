'''
Lecture 3
Topic: Morphological Erosion
This script applies Erosion to a binary version of the live feed.
Erosion removes pixels on object boundaries.
It makes bright regions shrink (erode). Useful for removing small white noise.
'''

import cv2
import numpy as np
from picamzero import Camera

# Initialize camera
cam = Camera()

print("Starting Erosion script. Press 'q' to exit.")

# Kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)

# Threshold for binary conversion
thresh_val = 127

try:
    while True:
        # Capture frame
        frame = cam.pc2.capture_array()

        # FIX: Check if frame has 4 channels (RGBA/BGRA) and convert to 3 channels (BGR)
        if frame.shape[2] == 4:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)

        # Convert to grayscale and then binary threshold
        # Morphology works best on binary images
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, thresh_val, 255, cv2.THRESH_BINARY)

        # Apply Erosion
        # iterations: how many times to apply the operation
        eroded = cv2.erode(binary, kernel, iterations=1)

        # Convert back to BGR for stacking
        binary_bgr = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
        eroded_bgr = cv2.cvtColor(eroded, cv2.COLOR_GRAY2BGR)

        # Stack images side-by-side
        combined = cv2.hconcat([binary_bgr, eroded_bgr])

        # Add text overlay
        cv2.putText(combined, "Erosion (White regions shrink)", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display
        cv2.imshow("Left: Binary Input | Right: Eroded", combined)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cv2.destroyAllWindows()

