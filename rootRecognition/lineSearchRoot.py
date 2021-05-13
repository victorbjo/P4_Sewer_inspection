import cv2
import numpy as np

from matplotlib import pyplot as plt
# load image
def findLines(img,start,output):

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    kernel_size = 5
    blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)
    low_threshold = 130
    high_threshold = 180
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
    rho = 0.4  # distance resolution in pixels of the Hough grid
    theta = np.pi / 160  # angular resolution in radians of the Hough grid
    threshold = 30  # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 10  # minimum number of pixels making up a line
    max_line_gap = 40  # maximum gap in pixels between connectable line segments
    line_image = np.copy(img) * 0  # creating a blank to draw lines on

    # Run Hough on edge detected image
    # Output "lines" is an array containing endpoints of detected line segments
    lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                        min_line_length, max_line_gap)

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(output,(x1,y1),(x2,y2),(255,2,100),5)
                # Draw the lines on the  image
    #lines_edges = cv2.addWeighted(output, 0, start, 1, 0)
    #print("okas")
    return ([lines])
   
