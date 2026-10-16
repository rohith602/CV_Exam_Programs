# Program 1: Python OpenCV Canny Edge Detection
# Run:    python Program_1_Canny_Edge_Detection.py
# Needs:  opencv-python
# Close:  click the picture window and press any key

# CHANGED from the record: work inside this program's own folder, so image.jpg
# is found whichever folder the program is started from (needed for double-click)
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import cv2

# CHANGED from the record: 'bird.png' became 'image.jpg' (one picture for all programs)
FILE_NAME = 'image.jpg'

# Read image from disk
img = cv2.imread(FILE_NAME)

# CHANGED from the record: added this check, so a missing picture gives a clear message
if img is None:
    print("Image not found!")
    exit()

# Canny edge detection
# 100 and 200 are the lower and upper thresholds for how strong an edge must be
edges = cv2.Canny(img, 100, 200)

# Display the edge image
cv2.imshow('Edges', edges)

cv2.waitKey(0)            # wait until a key is pressed
cv2.destroyAllWindows()   # then close the window
