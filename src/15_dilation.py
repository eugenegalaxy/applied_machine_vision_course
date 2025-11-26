'''
Lecture 3
Topic: Morphological Dilation
This script applies Dilation to a binary version of the live feed.
Dilation adds pixels to the boundaries of objects in an image.
It makes bright regions grow (dilate). Useful for joining broken parts of an object.
'''

import cv2
import numpy as np
from picamzero import Camera

# Initialize camera
cam = Camera()

print("Starting Dilation script. Press 'q' to exit.")

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

        # Apply Dilation
        # iterations: how many times to apply the operation
        dilated = cv2.dilate(binary, kernel, iterations=1)

        # Convert back to BGR for stacking
        binary_bgr = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
        dilated_bgr = cv2.cvtColor(dilated, cv2.COLOR_GRAY2BGR)

        # Stack images side-by-side
        combined = cv2.hconcat([binary_bgr, dilated_bgr])

        # Add text overlay
        cv2.putText(combined, "Dilation (White regions expand)", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display
        cv2.imshow("Left: Binary Input | Right: Dilated", combined)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cv2.destroyAllWindows()

