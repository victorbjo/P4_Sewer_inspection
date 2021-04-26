import cv2
import glob
import isolate
from matplotlib import pyplot as plt
import numpy as np


images = [cv2.imread(file) for file in glob.glob("f:/cracks/*.jpg")]
con = []
hsv = []
Tjek = []
im = []
im2 = []
im3 = []
kernelEllipse = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
kernelEllipse2 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
for i in range(len(images)):
    images[i] = isolate.findBackPlate(images[i])
    images[i] = cv2.resize(images[i], (int(images[i].shape[1] / 3), int(images[i].shape[0] / 3)))
    hsv.append(cv2.cvtColor(images[i], cv2.COLOR_BGR2HSV))
    con.append(np.zeros(hsv[i].shape))
    #Tjek.append(cv2.inRange(hsv[i], (100, 25, 30), (170, 130, 80)))
    Tjek.append(cv2.inRange(hsv[i], (0, 0, 0), (255, 255, 43)))
    im.append(cv2.morphologyEx(Tjek[i], cv2.MORPH_ERODE, kernelEllipse))
    # Tjek.append(cv2.inRange(hsv[i], (0, 0, 0), (36, 100, 255)))
    im2.append(cv2.morphologyEx(im[i], cv2.MORPH_DILATE, kernelEllipse2))
    #im3.append(cv2.morphologyEx(im2[i], cv2.MORPH_CLOSE, kernelEllipse2))
    contours, hierarchy = cv2.findContours(im2[i], cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(con[i], contours, -1, (0, 255, 0), 3)
    cv2.imshow("ss", images[i])
    cv2.waitKey(0)
    # Creates a morphology kernel of 7x7 size in the shape of an ellipse
    # plt.subplot(4, 3, i+1), plt.imshow(hsv[i])
# plt.show()

# for i in range(len(hsv)):
#   for y in range(len(hsv[i][1, :, :])):
#      for x in range(len(hsv[i][:, 1, :])):
#         im.append(hsv[i][x, y, :])


# cv2.imshow("hej", im[1])

# cv2.waitKey(0)
