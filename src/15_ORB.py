'''
Lecture 3
Topic: Feature Detection (ORB)
This script detects keypoints in the image using ORB (Oriented FAST and Rotated BRIEF).
ORB is a fast, rotation invariant feature detector (good alternative to SIFT/SURF).
Keypoints are interesting points in the image (corners, edges) that can be tracked.
'''

import cv2
import numpy as np
from picamzero import Camera

# Initialize camera
cam = Camera()

print("Starting ORB Feature Detection script. Press 'q' to exit.")

# Initialize ORB detector
# nfeatures: maximum number of features to retain
orb = cv2.ORB_create(nfeatures=500)

try:
    while True:
        # Capture frame
        frame = cam.pc2.capture_array()

        # FIX: Check if frame has 4 channels (RGBA/BGRA) and convert to 3 channels (BGR)
        if frame.shape[2] == 4:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)

        # Convert to grayscale (Detectors usually work on grayscale)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect keypoints
        # find the keypoints with ORB
        kp = orb.detect(gray, None)

        # Compute descriptors (optional, not needed just for drawing)
        # kp, des = orb.compute(gray, kp)

        # Draw keypoints on the original color image
        # color=(0,255,0): Green keypoints
        # flags=0: Draw only keypoints, not size and orientation
        img_keypoints = cv2.drawKeypoints(frame, kp, None, color=(0, 255, 0), flags=0)

        # Stack images side-by-side
        combined = cv2.hconcat([frame, img_keypoints])

        # Add text overlay
        cv2.putText(combined, f"ORB Keypoints: {len(kp)} detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display
        cv2.imshow("Left: Original | Right: ORB Features", combined)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cv2.destroyAllWindows()

