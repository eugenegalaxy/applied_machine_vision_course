'''
Lecture 2
Topic: Contrast Adjustment
This script increases the contrast of the live video feed.
Contrast is the difference in luminance or color that makes an object distinguishable.
'''

import cv2
import numpy as np
from picamzero import Camera

# Initialize camera
cam = Camera()

# Contrast factor (Alpha)
# 1.0 = original
# > 1.0 = higher contrast
# < 1.0 = lower contrast
alpha = 1.5 
beta = 0 # Brightness (no change)

print(f"Starting Contrast script (Alpha={alpha}). Press 'q' to exit.")

try:
    while True:
        # Capture frame
        frame = cam.pc2.capture_array()

        # FIX: Check if frame has 4 channels (RGBA/BGRA) and convert to 3 channels (BGR)
        if frame.shape[2] == 4:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)

        # Apply contrast adjustment: New = Alpha * Old + Beta
        # convertScaleAbs handles clamping to 0-255 automatically
        contrast_frame = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)

        # Stack images side-by-side
        combined = cv2.hconcat([frame, contrast_frame])

        # Display
        cv2.imshow(f"Left: Original | Right: Contrast factor = {alpha}", combined)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cv2.destroyAllWindows()

