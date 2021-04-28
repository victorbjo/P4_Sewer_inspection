import cv2
import glob
import isolate
img = [cv2.imread(file) for file in glob.glob("*.jpg")]

print(len(img))
for i in range (len(img)):
    #imgCopy = img[i].copy()
    img[i] = isolate.findBackPlate(img[i])
    img[i] = cv2.cvtColor(img[i],cv2.COLOR_BGR2HSV)
    imgCopy = img[i].copy()
    #img[i] = cv2.inRange(img[i],(50,0,0),(310,255,255))
    mask1 = cv2.inRange(img[i], (50, 0, 0), (200, 255,230))

    ## mask o yellow (15,0,0) ~ (36, 255, 255)
    mask2 = cv2.inRange(img[i], (360,0,0), (360, 255, 220))

    ## final mask and masked
    mask = cv2.bitwise_or(mask1, mask2)
    target = cv2.bitwise_and(imgCopy,imgCopy, mask=mask)
    target = cv2.cv2.cvtColor(target,cv2.COLOR_HSV2BGR)
    cv2.imshow("image",target)
    cv2.waitKey()
    

'''
import cv2
import numpy as np
import glob
import isolate
import lineSearch
from matplotlib import pyplot as plt
img = [cv2.imread(file) for file in glob.glob("*.jpg")]
for i in range (len(img)):
    img[i] = cv2.resize(img[i], (int(img[i].shape[1]/3), int(img[i].shape[0]/3)))
    try:
        lineSearch.findLines(img[i],img[i],img[i])
        print("YES")
    except:
        2
    img[i] = isolate.findBackPlate(img[i],1.5,250,40,100,100,200)
    img[i] = isolate.findBackPlate(img[i],1.5,250,110,78,120,1000)
    edges = cv2.Canny(img[i],100,200)

    plt.subplot(121),plt.imshow(img[i],cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    plt.show()
    cv2.waitKey()
#circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.5, 250,param1=40,param2=100,minRadius=100,maxRadius=200)
#circles = cv2.HoughCircles(grey, cv2.HOUGH_GRADIENT, 1.5, 250,param1=110,param2=78,minRadius=120,maxRadius=300)
'''
