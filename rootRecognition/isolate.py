import numpy as np
import cv2
def findBackPlate(img):
    grey = img.copy()
    grey= cv2.cvtColor(grey, cv2.COLOR_BGR2GRAY)
    output = img.copy()
    circles = cv2.HoughCircles(grey, cv2.HOUGH_GRADIENT, 1.5, 250,param1=110,param2=78,minRadius=120,maxRadius=300)

    if circles is not None and len(circles[0]) < 2:
        circles = np.round(circles[0, :]).astype("int")
            # loop over t67he (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            cv2.circle(output, (x, y), r, (0, 0, 0), -1)
           # cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)


    return (output=
