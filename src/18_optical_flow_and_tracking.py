'''
Lecture 4
Topic: Optical Flow and Tracking (Lucas-Kanade)
This script demonstrates Sparse Optical Flow using the Lucas-Kanade method.
It detects feature points (corners) and tracks them from frame to frame.
Press 'r' to re-detect points if tracking is lost.
'''

import cv2
import numpy as np
from picamzero import Camera

# Initialize camera
cam = Camera()

print("Starting Optical Flow script.")
print("Press 'q' to exit.")
print("Press 'r' to re-initialize tracking points.")

# Lucas-Kanade parameters
lk_params = dict(winSize=(15, 15),
                 maxLevel=2,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Feature detection parameters (Shi-Tomasi corner detector)
feature_params = dict(maxCorners=100,
                      qualityLevel=0.3,
                      minDistance=7,
                      blockSize=7)

# Tracks state
old_gray = None
p0 = None
mask = None

try:
    while True:
        # Capture frame
        frame = cam.pc2.capture_array()

        # FIX: Check if frame has 4 channels (RGBA/BGRA) and convert to 3 channels (BGR)
        if frame.shape[2] == 4:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)

        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Initialize if first run or requested
        if p0 is None:
            p0 = cv2.goodFeaturesToTrack(frame_gray, mask=None, **feature_params)
            old_gray = frame_gray.copy()
            # Create a mask image for drawing purposes
            mask = np.zeros_like(frame)
            
        # Calculate Optical Flow
        if p0 is not None and len(p0) > 0:
            p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

            # Select good points (st==1 means flow found)
            if p1 is not None:
                good_new = p1[st == 1]
                good_old = p0[st == 1]

                # Draw the tracks
                for i, (new, old) in enumerate(zip(good_new, good_old)):
                    a, b = new.ravel()
                    c, d = old.ravel()
                    # Draw line on mask (persistent)
                    mask = cv2.line(mask, (int(a), int(b)), (int(c), int(d)), (0, 255, 0), 2)
                    # Draw point on current frame
                    frame = cv2.circle(frame, (int(a), int(b)), 5, (0, 0, 255), -1)

                # Overlay mask on frame
                img = cv2.add(frame, mask)

                # Update the previous frame and previous points
                old_gray = frame_gray.copy()
                p0 = good_new.reshape(-1, 1, 2)
            else:
                img = frame
                p0 = None # Lost all points
        else:
            img = frame

        # Add info text
        cv2.putText(img, f"Tracks: {len(p0) if p0 is not None else 0} (Press 'r' to reset)", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display
        cv2.imshow("Optical Flow (Lucas-Kanade)", img)

        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            break
        elif k == ord('r'):
            p0 = None
            mask = np.zeros_like(frame)

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cv2.destroyAllWindows()

