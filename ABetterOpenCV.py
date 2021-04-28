import cv2
import numpy as np
from matplotlib import pyplot as plt
def threshold(img, l0, l1, l2, h0, h1, h2):
    newImg = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)
    #print(newImg.shape)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if (l0 < img[x][y][0] < h0 and l1 < img[x][y][1] < h1 and l2 < img[x][y][2] < h2):
                newImg[x][y] = 255
            else:
                newImg[x][y] = 0
            #print(img[x][y][0])
    return (newImg)

