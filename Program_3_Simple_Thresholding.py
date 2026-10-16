# Program 3: Python OpenCV Simple Thresholding
# Run:    python Program_3_Simple_Thresholding.py
# Needs:  opencv-python
# Close:  click any picture window and press any key (5 windows open)

# CHANGED from the record: work inside this program's own folder, so image.jpg
# is found whichever folder the program is started from (needed for double-click)
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import cv2

# Read image
# CHANGED from the record: "tree.jpg" became "image.jpg"
image = cv2.imread("image.jpg")

if image is None:
    print("Image not found!")
    exit()

# Convert to grayscale
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding techniques
# 120 is the threshold: each pixel is compared with it. 255 is white.
_, t1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
_, t2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
_, t3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
_, t4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
_, t5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

# Display smaller output frames
images = [
    ("Binary", t1),
    ("Binary Inverted", t2),
    ("Truncated", t3),
    ("Set to Zero", t4),
    ("Set to Zero Inverted", t5)
]

for name, result in images:
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, 300, 250)
    cv2.imshow(name, result)

cv2.waitKey(0)
cv2.destroyAllWindows()
