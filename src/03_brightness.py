'''
Lecture 2
Topic: Brightness Adjustment
This script increases the brightness of the live video feed.
Brightness refers to the overall lightness or darkness of the image.
'''

import cv2
import numpy as np
from picamzero import Camera

# Initialize camera
cam = Camera()

# Brightness increase (Beta)
# Positive value = brighter
# Negative value = darker
beta = 50
alpha = 1.0 # Contrast (no change)

print(f"Starting Brightness script (Beta={beta}). Press 'q' to exit.")

try:
    while True:
        # Capture frame
        frame = cam.pc2.capture_array()

        # Apply brightness adjustment: New = Alpha * Old + Beta
        bright_frame = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)

        # Stack images side-by-side
        combined = cv2.hconcat([frame, bright_frame])

        # Display
        cv2.imshow(f"Left: Original | Right: Brightness increase = {beta}", combined)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cv2.destroyAllWindows()

