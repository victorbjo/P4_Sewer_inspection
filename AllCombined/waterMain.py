import cv2
import numpy as np

from matplotlib import pyplot as plt
import lineSearch as lines
import distance
def getWater(image):
        # load image

        #print(image.shape)
        #print(image.shape[0])
        image = cv2.resize(image, (int(image.shape[1]/3), int(image.shape[0]/3)))

        output = image.copy()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # detect circles in the image
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.7, 250,param1=40,param2=110,minRadius=80,maxRadius=200)
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
        else:
                print("OK")
                #cv2.imshow("output", np.hstack([image, output]))
                #cv2.waitKey(0)
        maxX = x-r
        if maxX < 0:
                maxX = 0
        crop = output[y-r:y+r, maxX:x+r]
        try:
                line = (lines.findLines(crop,image,output,x-r,y-r,r))
                result= distance.calcWater(line,x,y,r,crop,image,output)
        except:
               result = 0

                   
        #cv2.imshow("output", np.hstack([image, output]))
        #cv2.waitKey(0)
        return result
        
#image = cv2.imread("pictures/roots11.jpg")
#a = getWater(image)
#print ("Water level: "+str(a)+"%")
