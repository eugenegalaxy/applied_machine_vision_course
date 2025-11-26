'''
Lecture 2
Topic: Background Subtraction
This script segments the moving foreground objects from the static background.
It learns the background model over time and subtracts it to find changes.
'''

import cv2
import numpy as np
from picamzero import Camera

# Initialize camera
cam = Camera()

# Initialize Background Subtractor
# MOG2 is a common Gaussian Mixture-based Background/Foreground Segmentation Algorithm
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)

print("Starting Background Subtraction script. Press 'q' to exit.")

try:
    while True:
        # Capture frame
        frame = cam.pc2.capture_array()

        # Apply background subtraction
        # returns a mask where 0=background, 255=foreground, 127=shadow (if detectShadows=True)
        fgmask = fgbg.apply(frame)

        # Convert mask to BGR for stacking
        fgmask_bgr = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2BGR)

        # Stack images side-by-side
        combined = cv2.hconcat([frame, fgmask_bgr])

        # Display
        cv2.imshow("Left: Original | Right: Foreground Mask", combined)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cv2.destroyAllWindows()
