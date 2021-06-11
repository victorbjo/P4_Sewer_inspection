import cv2
import numpy as np
import glob
import isolate
from matplotlib import pyplot as plt
def checkForRoots(img):
    img = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))
    imgCopy = img.copy()
    img = isolate.findBackPlate(img,1.4,200,180,90,50,int(imgCopy.shape[1]/1.1))
    img = isolate.findBackPlate(img,1.4,250,200,78,40,int(imgCopy.shape[1]/1.1))
    edges = cv2.Canny(img,100,200)
    plt.subplot(131),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    edges = edges[0:int(edges.shape[0]/2), 0:edges.shape[1]]
    hist = cv2.calcHist([edges],[0],None,[256],[0,256])
    print(hist[-1]/hist[0])
    #Returns true if white to black pixel radius is above 0.0304
    return (hist[-1]/hist[0] > 0.0304)
