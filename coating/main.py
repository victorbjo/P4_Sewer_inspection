import cv2
import glob
import numpy as np
from matplotlib import pyplot as plt
import math

def getCoating (img):
    images = []
    #images = [cv2.imread(file) for file in glob.glob("*.PNG")] + [cv2.imread(file) for file in glob.glob("*.JPG")]
    images.append(img)

    isCoating = 0
    
    thresh = []
    edge = []
    morph_open = []
    morph_erode = []
    morph_close = []
    img_contours = []
    print(len(images))
    for i in range(len(images)):
        images[i] = cv2.resize(images[i], (int(images[i].shape[1] /3), int(images[i].shape[0]/3)))

        images[i] = cv2.cvtColor(images[i], cv2.COLOR_BGR2HSV)
        thresh.append(cv2.inRange(images[i], (100,20,0), (140,255,255)))

        
        # Morphologi
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
        morph_open.append(cv2.morphologyEx(thresh[i], cv2.MORPH_OPEN, kernel, iterations=1))
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        morph_erode.append(cv2.morphologyEx(morph_open[i], cv2.MORPH_ERODE, kernel))
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        morph_close.append(cv2.morphologyEx(morph_erode[i], cv2.MORPH_CLOSE, kernel, iterations=1))

        # contours
        contours, hierarchy = cv2.findContours(morph_close[i], cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        img_contours.append(np.zeros(images[i].shape))

        # features
        contourIndex = np.zeros(len(contours))
        area = np.zeros(len(contours))
        perimeter = np.zeros(len(contours))
        circularity = np.zeros(len(contours))
        elongation = np.zeros(len(contours))
        
        for j in range(len(contours)):
            if hierarchy[0][j][3] == -1:
                contourIndex[j] = j
                area[j] = cv2.contourArea((contours[j]))
                perimeter[j] = cv2.arcLength(contours[j], 1)
                circularity[j] = (4 * 3.14 * area[j]) / (int(perimeter[j]) ** 2)
                
                rect = cv2.minAreaRect(contours[j])
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                elongation[j] = cv2.max(int(rect[1][0]) / int(rect[1][1]), int(rect[1][1]) / int(rect[1][0]))[0]

                if  area[j] > 150 and circularity[j] < 0.3 and perimeter[j] > 200 and elongation [j] > 2.5:
                    cv2.drawContours(img_contours[i], contours, int(contourIndex[j]), (0,255,255), 3)
                    cv2.drawContours(img_contours[i], [box], 0, (0,255,255), 2)
                    print(elongation[j])
                    isCoating = 1
        cv2.imshow("a", img_contours[i])
        cv2.waitKey(0)
        return isCoating

print(getCoating(cv2.imread("1_coating.PNG")))
