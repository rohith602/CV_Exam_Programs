# Program 5: Python program to demonstrate erosion and dilation of images
# Run:    python Program_5_Erosion_Dilation.py
# Needs:  opencv-python, numpy
# Close:  click any picture window and press any key (3 windows open)

# CHANGED from the record: work inside this program's own folder, so image.jpg
# is found whichever folder the program is started from (needed for double-click)
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import cv2
import numpy as np

# Read grayscale image (the 0 means "load in grey")
# CHANGED from the record: "tree.jpg" became "image.jpg"
img = cv2.imread("image.jpg", 0)

if img is None:
    print("Image not found!")
    exit()

# Create kernel (a 5x5 block of ones: the neighbourhood each pixel is compared with)
kernel = np.ones((5, 5), np.uint8)

# Erosion and Dilation
erosion = cv2.erode(img, kernel, iterations=1)     # bright areas shrink
dilation = cv2.dilate(img, kernel, iterations=1)   # bright areas grow

# Display smaller windows
images = [
    ("Original", img),
    ("Erosion", erosion),
    ("Dilation", dilation)
]

for name, result in images:
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, 300, 250)
    cv2.imshow(name, result)

cv2.waitKey(0)
cv2.destroyAllWindows()
