'''
Lecture 4
Topic: Forward Image Warping
This script demonstrates "Forward Warping".
In forward warping, we iterate over SOURCE pixels and calculate their new position in the DESTINATION image.
pixels_dst[T(x, y)] = pixels_src[x, y]

Problem: This approach often leaves "holes" or gaps in the destination image because
multiple source pixels might not map to every single destination pixel after transformation.
This script visualizes those holes by performing a simple rotation.
'''

import cv2
import numpy as np
from picamzero import Camera

# Initialize camera
cam = Camera()

print("Starting Forward Warping script. Press 'q' to exit.")

def forward_rotate(image, angle_deg):
    h, w = image.shape[:2]
    
    # Create black destination image
    # Making it slightly larger to hold rotated image or just clip it
    dst = np.zeros_like(image)
    
    # Calculate rotation matrix (Center of image)
    center = (w // 2, h // 2)
    angle_rad = np.radians(angle_deg)
    
    # Simple Rotation Matrix [[cos, -sin], [sin, cos]]
    # We need to offset by center to rotate around center
    cos_a = np.cos(angle_rad)
    sin_a = np.sin(angle_rad)
    
    # Create grid of (x, y) coordinates
    # indices is (2, h, w) -> (y, x) grid
    y, x = np.indices((h, w))
    
    # Shift to center
    x_c = x - center[0]
    y_c = y - center[1]
    
    # Apply Rotation (Forward Mapping)
    # x' = x*cos - y*sin
    # y' = x*sin + y*cos
    x_new = (x_c * cos_a - y_c * sin_a) + center[0]
    y_new = (x_c * sin_a + y_c * cos_a) + center[1]
    
    # Round to nearest integer (nearest neighbor)
    x_new = np.rint(x_new).astype(int)
    y_new = np.rint(y_new).astype(int)
    
    # Filter out points that fall outside the image boundaries
    mask = (x_new >= 0) & (x_new < w) & (y_new >= 0) & (y_new < h)
    
    # Assign pixels
    # dst[y', x'] = src[y, x]
    # Using vectorized indexing for speed (Python loops would be too slow)
    dst[y_new[mask], x_new[mask]] = image[y[mask], x[mask]]
    
    return dst

try:
    angle = 0
    while True:
        # Capture frame
        frame = cam.pc2.capture_array()

        # FIX: Check if frame has 4 channels (RGBA/BGRA) and convert to 3 channels (BGR)
        if frame.shape[2] == 4:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)

        # Downscale for performance and to make holes more visible
        small_frame = cv2.resize(frame, (320, 240))
        
        # Increment angle
        angle = (angle + 1) % 360
        
        # Perform Forward Warping
        warped = forward_rotate(small_frame, angle)

        # Resize back up for display (nearest neighbor to keep the "pixelated/holey" look)
        warped_display = cv2.resize(warped, (frame.shape[1], frame.shape[0]), interpolation=cv2.INTER_NEAREST)
        
        # Stack images
        combined = cv2.hconcat([frame, warped_display])

        # Add text
        cv2.putText(combined, "Forward Warping (Notice black holes/dots)", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display
        cv2.imshow("Left: Original | Right: Forward Warp", combined)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cv2.destroyAllWindows()

