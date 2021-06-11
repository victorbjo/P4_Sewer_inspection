import cv2
import numpy as np

from matplotlib import pyplot as plt
import lineSearch as lines
import distance
def getWater(image):
        # load image
        image = cv2.resize(image, (int(image.shape[1]/3), int(image.shape[0]/3)))
        output = image.copy()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # detect circles in the image
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.5, 250,param1=40,param2=100,minRadius=100,maxRadius=200)
        # ensure at least some circles were found
        if circles is not None:
                # convert the (x, y) coordinates and radius of the circles to integers
                circles = np.round(circles[0, :]).astype("int")
                # loop over t67he (x, y) coordinates and radius of the circles
                for (x, y, r) in circles:
                        # draw the circle in the output image, then draw a rectangle
                        # corresponding to the center of the circle
                        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
                        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
                        
                        #print(x,y,r)
        crop = output[y-r:y+r, x-r:x+r]
        #Tries to find lines
        try:
                line = (lines.findLines(crop,image,output,x-r,y-r,r))
                result= distance.calcWater(line,x,y,r,crop,image,output)
        except:
               result = 0
        return result