'''
Lecture 2
Topic: Image Histogram
This script computes and displays the histogram of the live video feed.
A histogram represents the distribution of pixel intensities in the image.
'''

import cv2
import numpy as np
from picamzero import Camera

# Initialize camera
cam = Camera()

print("Starting Histogram script. Press 'q' to exit.")

def draw_histogram(img, color=(255, 255, 255)):
    # Convert to grayscale for simple intensity histogram
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Calculate histogram
    # images, channels, mask, histSize, ranges
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    
    # Create an image to draw the histogram on
    hist_h, hist_w = 400, 512
    hist_img = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
    
    # Normalize histogram to fit in the image height
    cv2.normalize(hist, hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
    
    # Draw lines for the histogram
    for i in range(1, 256):
        # Point 1: (x, y) - Note: y is inverted because image origin is top-left
        pt1 = (int((i - 1) * (hist_w / 256)), hist_h - int(hist[i - 1]))
        pt2 = (int(i * (hist_w / 256)), hist_h - int(hist[i]))
        cv2.line(hist_img, pt1, pt2, color, thickness=2)
        
    return hist_img

try:
    while True:
        # Capture frame
        frame = cam.pc2.capture_array()

        # Resize frame to match histogram height for cleaner stacking (optional but looks better)
        # Let's just resize the histogram image to match the frame height if needed, 
        # or resize frame to fixed width. 
        # For simplicity, we'll just resize the histogram plot to match frame height.
        h, w = frame.shape[:2]
        hist_img = draw_histogram(frame)
        hist_img_resized = cv2.resize(hist_img, (w, h))

        # Stack images side-by-side
        combined = cv2.hconcat([frame, hist_img_resized])

        # Display
        cv2.imshow("Left: Original | Right: Histogram", combined)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cv2.destroyAllWindows()

