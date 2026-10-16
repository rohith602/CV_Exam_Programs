# Program 4: Image blurring python program
# Run:    python Program_4_Image_Blurring.py
# Needs:  opencv-python
# Close:  click any picture window and press any key (4 windows open)

# CHANGED from the record: work inside this program's own folder, so image.jpg
# is found whichever folder the program is started from (needed for double-click)
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import cv2

# Read image
# CHANGED from the record: "tree.jpg" became "image.jpg"
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
    exit()

# Gaussian Blur (7x7 neighbourhood, weighted so nearer pixels count more)
gaussian = cv2.GaussianBlur(img, (7, 7), 0)

# Median Blur (each pixel becomes the middle value of its 5x5 neighbourhood)
median = cv2.medianBlur(img, 5)

# Bilateral Blur (smooths flat areas but keeps edges sharp)
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

# Display results in smaller windows
images = [
    ("Original", img),
    ("Gaussian Blur", gaussian),
    ("Median Blur", median),
    ("Bilateral Blur", bilateral)
]

for name, result in images:
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, 300, 250)
    cv2.imshow(name, result)

cv2.waitKey(0)
cv2.destroyAllWindows()
