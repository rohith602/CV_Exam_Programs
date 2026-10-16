# Program 2: Sobel, Prewitt, Laplacian and Canny edge detection side-by-side
# Run:    python Program_2_Edge_Detection_Comparison.py
# Needs:  opencv-python, numpy
# Close:  click any picture window and press any key (5 windows open)

# CHANGED from the record: work inside this program's own folder, so image.jpg
# is found whichever folder the program is started from (needed for double-click)
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import cv2
import numpy as np

# Read image
# CHANGED from the record: "tree.jpg" became "image.jpg"
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 1. Sobel
sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)   # change in the x direction
sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)   # change in the y direction
sobel = cv2.addWeighted(cv2.convertScaleAbs(sx), 0.5,
                        cv2.convertScaleAbs(sy), 0.5, 0)

# 2. Prewitt (OpenCV has no Prewitt function, so the two kernels are written by hand)
px = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
py = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

prewitt_x = cv2.filter2D(gray, cv2.CV_32F, px)
prewitt_y = cv2.filter2D(gray, cv2.CV_32F, py)
prewitt = cv2.addWeighted(
    cv2.convertScaleAbs(prewitt_x), 0.5,
    cv2.convertScaleAbs(prewitt_y), 0.5, 0
)

# 3. Laplacian
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = cv2.convertScaleAbs(lap)

# 4. Canny
canny = cv2.Canny(gray, 100, 200)

# Display smaller frames
images = [
    ("Original", img),
    ("Sobel", sobel),
    ("Prewitt", prewitt),
    ("Laplacian", lap),
    ("Canny", canny)
]

for name, result in images:
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, 300, 250)
    cv2.imshow(name, result)

cv2.waitKey(0)
cv2.destroyAllWindows()
