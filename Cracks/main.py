import cv2
import glob
import isolate
from matplotlib import pyplot as plt
import numpy as np

#load images
images = [cv2.imread(file) for file in glob.glob("f:/git 2/Cracks/2/*.jpg")]

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

    #isolate backplate and resize images
    images[i] = isolate.findBackPlate(images[i])
    images[i] = cv2.resize(images[i], (int(images[i].shape[1] / 3), int(images[i].shape[0] / 3)))

    #convert to HSV
    hsv.append(cv2.cvtColor(images[i], cv2.COLOR_BGR2HSV))

    #empty pics for contour
    con.append(np.zeros(hsv[i].shape))
    #Tjek.append(cv2.inRange(hsv[i], (100, 25, 30), (170, 130, 80)))

    #thredshold
    Tjek.append(cv2.inRange(hsv[i], (0, 0, 0), (255, 255, 43)))

    #morphology
    im.append(cv2.morphologyEx(Tjek[i], cv2.MORPH_ERODE, kernelEllipse))
    im2.append(cv2.morphologyEx(im[i], cv2.MORPH_DILATE, kernelEllipse2))
    #im3.append(cv2.morphologyEx(im2[i], cv2.MORPH_CLOSE, kernelEllipse2))

    #find contour
    contours, hierarchy = cv2.findContours(im2[i], cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #draw contour in empty pics
    cv2.drawContours(con[i], contours, -1, (0, 255, 0), 3)

    #show pic/contour
    cv2.imshow("ss", con[i])
    print("AHH SHIET")
    cv2.waitKey(0)
    # plt.subplot(4, 3, i+1), plt.imshow(hsv[i])
# plt.show()

# for i in range(len(hsv)):
#   for y in range(len(hsv[i][1, :, :])):
#      for x in range(len(hsv[i][:, 1, :])):
#         im.append(hsv[i][x, y, :])


# cv2.imshow("hej", im[1])

# cv2.waitKey(0)
