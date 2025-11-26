'''
Lecture 2
Topic: Thresholding
This script converts the image to a binary image (black and white only).
It separates "object" pixels (white) from "background/noise" pixels (black) based on a threshold value.
'''

import cv2
import numpy as np
from picamzero import Camera

# Initialize camera
cam = Camera()

# Threshold value (0-255)
thresh_val = 127

print(f"Starting Thresholding script (Threshold={thresh_val}). Press 'q' to exit.")

try:
    while True:
        # Capture frame
        frame = cam.pc2.capture_array()

        # FIX: Check if frame has 4 channels (RGBA/BGRA) and convert to 3 channels (BGR)
        if frame.shape[2] == 4:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)

        # Convert to grayscale (thresholding is typically done on grayscale images)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply Binary Thresholding
        # ret is the threshold value used (useful for Otsu's), binary is the result image
        ret, binary = cv2.threshold(gray, thresh_val, 255, cv2.THRESH_BINARY)

        # Convert binary to BGR for stacking
        binary_bgr = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
        
        # Convert original gray to BGR for comparison
        gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

        # Stack images side-by-side
        combined = cv2.hconcat([gray_bgr, binary_bgr])

        # Display
        cv2.imshow(f"Left: Grayscale | Right: Binary Threshold ({thresh_val})", combined)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cv2.destroyAllWindows()

