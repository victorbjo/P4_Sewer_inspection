import cv2
import glob
import isolateCrack as isolate
from matplotlib import pyplot as plt
import numpy as np
def findCracks(pic):
    #load images
    images = [pic]

    #declare vectors
    con = []
    hsv = []
    Tjek = []
    im = []
    im2 = []
    im3 = []

    #kernel for morphology
    kernelEllipse = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    kernelEllipse2 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    #for loop for looping through the images
    for i in range(len(images)):
        # print(i+1)
        knak = 0


        cv2.destroyAllWindows()
        #isolate backplate and resize images
        images[i] = isolate.findBackPlate(images[i])
        images[i] = cv2.resize(images[i], (int(images[i].shape[1] / 3), int(images[i].shape[0] / 3)))

        #convert to HSV
        hsv.append(cv2.cvtColor(images[i], cv2.COLOR_BGR2HSV))

        #empty pics for contour
        con.append(np.zeros(hsv[i].shape))
       

        #thredshold
        Tjek.append(cv2.inRange(hsv[i], (30, 120, 0), (179, 255, 50)))

        #morphology
        im.append(cv2.morphologyEx(Tjek[i], cv2.MORPH_ERODE, kernelEllipse))
        im2.append(cv2.morphologyEx(im[i], cv2.MORPH_DILATE, kernelEllipse2))
        #im3.append(cv2.morphologyEx(im2[i], cv2.MORPH_CLOSE, kernelEllipse2))

        #find contour
        contours, hierarchy = cv2.findContours(im2[i], cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        area = np.zeros(len(contours))
        arc = np.zeros(len(contours))
        circularity = np.zeros(len(contours))
        #find area
        if contours:
            for j in range (len(contours)):
                area[j] = cv2.contourArea((contours[j]))
                arc[j] = cv2.arcLength(contours[j], 1)
                circularity[j] = (4 * 3.14 * area[j]) / (int(arc[j]) ** 2)
                if 50 < cv2.contourArea(contours[j]) < 1200:
                    if 0.11 < circularity[j] < 0.88:
                        if 0.31 < arc[j] < 351:
                           
                            knak = 1
                            
    return (knak)



