import cv2
import glob
import  numpy as np
from matplotlib import pyplot as plt

def getOffset (img):
    images = []
    images.append(img)

    
    img_crop = []
    green = []
    green_eq = []
    thresh = []
    thresh_eq = []
    morph_open = []
    morph_close = []

    isOffset = 0
    
    img_contours = []
    area_feature = []
    perimeter_feature = []
    circularity_feature = []
    hasHole_feature = []
    elongation_feature = []
    counter = 0
    for i in range(len(images)):
        img_crop.append(img)

        green.append(img_crop[i][:,:,1])

        green_eq.append(cv2.equalizeHist(green[i]))

        # thresholding
        thresh_low = 1
        thresh_high = 15
        thresh.append(cv2.inRange(green[i], thresh_low, thresh_high))
        thresh_eq.append(cv2.inRange(green_eq[i], thresh_low, thresh_high))

        # morphology
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        morph_open.append(cv2.morphologyEx(thresh[i], cv2.MORPH_OPEN, kernel, iterations=1))
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (55, 55))
        morph_close.append(cv2.morphologyEx(morph_open[i], cv2.MORPH_CLOSE, kernel, iterations=1))

        # contours
        contours, hierarchy = cv2.findContours(morph_close[i], cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        img_contours.append(np.zeros(img_crop[i].shape))

        contourIndex = np.zeros(len(contours))
        area = np.zeros(len(contours))
        perimeter = np.zeros(len(contours))
        circularity = np.zeros(len(contours))

        # features
        for j in range(len(contours)):
            if hierarchy[0][j][3] == -1:
                contourIndex[j] = j
                area[j] = cv2.contourArea((contours[j]))
                perimeter[j] = cv2.arcLength(contours[j], 1)
                circularity[j] = (4 * 3.14 * area[j]) / (int(perimeter[j]) ** 2)

                rect = cv2.minAreaRect(contours[j])
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                
                if area[j] > 3000 and circularity[j] < 0.4 and circularity[j] > 0.03:
                    cv2.drawContours(img_contours[i], contours, int(contourIndex[j]), (0,255,255), 3)
                    cv2.drawContours(img_contours[i], [box], 0, (0,255,255), 3)
                    isOffset = 1
                    
        img_contours[i] =  cv2.resize(img_contours  [i], (int(img_contours[i].shape[1] /3), int(img_contours[i].shape[0]/3)))
        
        #print(i, " :", perimeter)
        #cv2.imshow("a",img_contours[i])
        #cv2.waitKey()

    #print("circularity: ", elongation)
        return isOffset
    
#print(getOffset(cv2.imread("1_offset.PNG")))

    #area_feature.append(max(area))
    #print("area: ", max(area))


testing = 1
if not testing:

    plt.subplot(4,2,1),plt.imshow(green[0])
    plt.subplot(4,2,2),plt.imshow(green_eq[0])

    plt.subplot(4,2,3),plt.imshow(green[1])
    plt.subplot(4,2,4),plt.imshow(green_eq[1])

    plt.subplot(4,2,5),plt.imshow(green[2])
    plt.subplot(4,2,6),plt.imshow(green_eq[2])

    plt.subplot(4,2,7),plt.imshow(green[3])
    plt.subplot(4,2,8),plt.imshow(green_eq[3])

    plt.show()

    plt.subplot(4,3,1),plt.imshow(thresh[0])
    plt.subplot(4,3,2),plt.imshow(thresh_eq[0])
    plt.subplot(4,3,3),plt.imshow(images[0])

    plt.subplot(4,3,4),plt.imshow(thresh[1])
    plt.subplot(4,3,5),plt.imshow(thresh_eq[1])
    plt.subplot(4,3,6),plt.imshow(images[1])

    plt.subplot(4,3,7),plt.imshow(thresh[2])
    plt.subplot(4,3,8),plt.imshow(thresh_eq[2])
    plt.subplot(4,3,9),plt.imshow(images[2])

    plt.subplot(4,3,10),plt.imshow(thresh[3])
    plt.subplot(4,3,11),plt.imshow(thresh_eq[3])
    plt.subplot(4,3,12),plt.imshow(images[3])

    plt.show()

    plt.subplot(4,3,1),plt.imshow(morph_open[0])
    plt.subplot(4,3,2),plt.imshow(morph_close[0])
    plt.subplot(4,3,3),plt.imshow(images[0])

    plt.subplot(4,3,4),plt.imshow(morph_open[1])
    plt.subplot(4,3,5),plt.imshow(morph_close[1])
    plt.subplot(4,3,6),plt.imshow(images[1])

    plt.subplot(4,3,7),plt.imshow(morph_open[2])
    plt.subplot(4,3,8),plt.imshow(morph_close[2])
    plt.subplot(4,3,9),plt.imshow(images[2])

    plt.subplot(4,3,10),plt.imshow(morph_open[3])
    plt.subplot(4,3,11),plt.imshow(morph_close[3])
    plt.subplot(4,3,12),plt.imshow(images[3])

    plt.show()






    plt.subplot(3,2,1),plt.imshow(green[4])
    plt.subplot(3,2,2),plt.imshow(green_eq[4])

    plt.subplot(3,2,3),plt.imshow(green[5])
    plt.subplot(3,2,4),plt.imshow(green_eq[5])

    plt.subplot(3,2,5),plt.imshow(green[6])
    plt.subplot(3,2,6),plt.imshow(green_eq[6])

    plt.show()

    plt.subplot(3,3,1),plt.imshow(thresh[4])
    plt.subplot(3,3,2),plt.imshow(thresh_eq[4])
    plt.subplot(3,3,3),plt.imshow(images[4])

    plt.subplot(3,3,4),plt.imshow(thresh[5])
    plt.subplot(3,3,5),plt.imshow(thresh_eq[5])
    plt.subplot(3,3,6),plt.imshow(images[5])

    plt.subplot(3,3,7),plt.imshow(thresh[6])
    plt.subplot(3,3,8),plt.imshow(thresh_eq[6])
    plt.subplot(3,3,9),plt.imshow(images[6])


    plt.show()

    plt.subplot(3,3,1),plt.imshow(morph_open[4])
    plt.subplot(3,3,2),plt.imshow(morph_close[4])
    plt.subplot(3,3,3),plt.imshow(images[4])

    plt.subplot(3,3,4),plt.imshow(morph_open[5])
    plt.subplot(3,3,5),plt.imshow(morph_close[5])
    plt.subplot(3,3,6),plt.imshow(images[5])

    plt.subplot(3,3,7),plt.imshow(morph_open[6])
    plt.subplot(3,3,8),plt.imshow(morph_close[6])
    plt.subplot(3,3,9),plt.imshow(images[6])

    plt.show()

    plt.subplot(4,2,1),plt.imshow(img_contours[0])
    plt.subplot(4,2,2),plt.imshow(img_contours[1])
    plt.subplot(4,2,3),plt.imshow(img_contours[2])
    plt.subplot(4,2,4),plt.imshow(img_contours[3])
    plt.subplot(4,2,5),plt.imshow(img_contours[4])
    plt.subplot(4,2,6),plt.imshow(img_contours[5])
    plt.subplot(4,2,7),plt.imshow(img_contours[6])

    plt.show()
