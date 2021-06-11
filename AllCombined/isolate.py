import numpy as np
import cv2
def findBackPlate(img,dp,min_dist,param1,param2,min_radius,max_radius):
    try:
        grey = img.copy()
        grey= cv2.cvtColor(grey, cv2.COLOR_BGR2GRAY)
        output = img.copy()
        #Finds all cirlces, with specific perimeters
        circles = cv2.HoughCircles(grey, cv2.HOUGH_GRADIENT, dp, min_dist,param1=param1,param2=param2,minRadius=min_radius,maxRadius=max_radius)
        #If circles are present:
        if circles is not None and len(circles[0]) < 2:
            #Converts all circle parameters to int
            circles = np.round(circles[0, :]).astype("int")
                # loop over the (x, y) coordinates and radius of the circles
            for (x, y, r) in circles:
                # draw the circle in the output image, then draw a rectangle
                # corresponding to the center of the circle
                cv2.circle(output, (x, y), r, (0, 0, 0), -1)
                cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
                #print(r)
    except:
        output = img
    return (output)
