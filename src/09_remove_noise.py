'''
Lecture 3
Topic: Noise Removal (Bilateral Filter)
This script demonstrates noise removal using a Bilateral Filter.
Bilateral filtering is highly effective at noise removal while preserving edges, 
unlike standard Gaussian blur which blurs edges too.
'''

import cv2
import numpy as np
from picamzero import Camera

# Initialize camera
cam = Camera()

print("Starting Noise Removal script. Press 'q' to exit.")

try:
    while True:
        # Capture frame
        frame = cam.pc2.capture_array()

        # FIX: Check if frame has 4 channels (RGBA/BGRA) and convert to 3 channels (BGR)
        if frame.shape[2] == 4:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)

        # Apply Bilateral Filter
        # d: Diameter of each pixel neighborhood (negative -> computed from sigmaSpace)
        # sigmaColor: Filter sigma in the color space (larger value means farther colors are mixed)
        # sigmaSpace: Filter sigma in the coordinate space (larger value means farther pixels affect each other)
        # Note: This can be computationally expensive on RPi!
        denoised = cv2.bilateralFilter(frame, d=9, sigmaColor=75, sigmaSpace=75)

        # Stack images side-by-side
        combined = cv2.hconcat([frame, denoised])

        # Add text overlay
        cv2.putText(combined, "Bilateral Filter (Edge Preserving)", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display
        cv2.imshow("Left: Original | Right: Denoised", combined)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cv2.destroyAllWindows()

