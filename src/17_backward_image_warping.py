'''
Lecture 4
Topic: Backward Image Warping
This script demonstrates "Backward Warping".
In backward warping, we iterate over DESTINATION pixels and calculate which SOURCE pixel to sample from.
pixels_dst[x, y] = pixels_src[T^-1(x, y)]

This is the standard approach in computer vision (like cv2.warpAffine) because it guarantees
every destination pixel gets a value (no holes), using interpolation (bilinear, etc.) for non-integer coordinates.
'''

import cv2
import numpy as np
from picamzero import Camera

# Initialize camera
cam = Camera()

print("Starting Backward Warping script. Press 'q' to exit.")

try:
    angle = 0
    while True:
        # Capture frame
        frame = cam.pc2.capture_array()

        # FIX: Check if frame has 4 channels (RGBA/BGRA) and convert to 3 channels (BGR)
        if frame.shape[2] == 4:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)

        h, w = frame.shape[:2]
        center = (w // 2, h // 2)
        
        # Increment angle
        angle = (angle + 1) % 360
        
        # Calculate Rotation Matrix (2x3)
        # cv2.getRotationMatrix2D creates the matrix for BACKWARD mapping logic internally
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        
        # Apply Affine Transformation (Backward Warping)
        # cv2.warpAffine iterates over destination pixels and interpolates from source
        warped = cv2.warpAffine(frame, M, (w, h))

        # Stack images
        combined = cv2.hconcat([frame, warped])

        # Add text
        cv2.putText(combined, "Backward Warping (Smooth, No holes)", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display
        cv2.imshow("Left: Original | Right: Backward Warp", combined)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cv2.destroyAllWindows()

