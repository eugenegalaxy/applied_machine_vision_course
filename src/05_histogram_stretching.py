'''
Lecture 2
Topic: Histogram Stretching (Contrast Stretching)
This script improves the contrast of the image by stretching the range of intensity values.
It makes the darkest pixel 0 and the brightest pixel 255, scaling everything in between.
'''

import cv2
import numpy as np
from picamzero import Camera

# Initialize camera
cam = Camera()

print("Starting Histogram Stretching script. Press 'q' to exit.")

try:
    while True:
        # Capture frame
        frame = cam.pc2.capture_array()

        # Convert to grayscale for simple stretching (or stretch V channel in HSV)
        # Here we stretch the grayscale version for visualization
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Find min and max pixel values
        min_val = np.min(gray)
        max_val = np.max(gray)

        # Avoid division by zero if image is solid color
        if max_val - min_val > 0:
            # Apply Min-Max Stretching: (pixel - min) * (255 / (max - min))
            # We use cv2.normalize which is faster and cleaner
            stretched = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)
        else:
            stretched = gray

        # Convert back to BGR for stacking
        stretched_bgr = cv2.cvtColor(stretched, cv2.COLOR_GRAY2BGR)
        
        # Also show the original gray for comparison
        gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

        # Stack images side-by-side
        combined = cv2.hconcat([gray_bgr, stretched_bgr])

        # Display
        cv2.imshow(f"Left: Original Gray | Right: Stretched (Min:{min_val}, Max:{max_val})", combined)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cv2.destroyAllWindows()

