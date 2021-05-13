import cv2
import glob
import isolate
from matplotlib import pyplot as plt
import numpy as np
def findcracks(pic):
    #load images
    #images = [cv2.imread(file) for file in glob.glob("C:/git/P4_Sewer_inspection/Cracks/2/*.jpg")]
    #images = [cv2.imread(file) for file in glob.glob(pic)]
    images = pic
    #print(len(images))
    #declare vectors
    con = []
    hsv = []
    Tjek = []
    im = []
    im2 = []
    im3 = []
    knak = 0
    #kernel for morphology
    kernelEllipse = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    kernelEllipse2 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    #for loop for looping through the images
    for i in range(len(images)):
       # print(i+1)
        cv2.destroyAllWindows()
        #isolate backplate and resize images
        images[i] = isolate.findBackPlate(images[i])
        images[i] = cv2.resize(images[i], (int(images[i].shape[1] / 3), int(images[i].shape[0] / 3)))

        #convert to HSV
        hsv.append(cv2.cvtColor(images[i], cv2.COLOR_BGR2HSV))

        #empty pics for contour
        con.append(np.zeros(hsv[i].shape))
        #Tjek.append(cv2.inRange(hsv[i], (100, 25, 30), (170, 130, 80)))

        #thredshold
        Tjek.append(cv2.inRange(hsv[i], (0, 30, 0), (255, 255, 43)))

        #morphology
        im.append(cv2.morphologyEx(Tjek[i], cv2.MORPH_ERODE, kernelEllipse))
        im2.append(cv2.morphologyEx(im[i], cv2.MORPH_DILATE, kernelEllipse2))
        #im3.append(cv2.morphologyEx(im2[i], cv2.MORPH_CLOSE, kernelEllipse2))

        #find contour
        contours, hierarchy = cv2.findContours(im2[i], cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        area = []
        arc = []
        #find area
        if contours:
            for j in range (len(contours)):
                if 350 < cv2.contourArea(contours[j]) < 800:
                    area.append(cv2.contourArea(contours[j]))
                    if cv2.arcLength(contours[j], True) < 200:
                        arc.append(cv2.arcLength(contours[j], True))
                        # draw contour in empty pics
                        cv2.drawContours(images[i], contours, j, (0, 255, 0), 1)
                        #print("AHH SHIET")
                        #print(area)
                        #print(arc)
                        #cv2.imshow("ss", images[i])
                        Knak = 1
                        cv2.waitKey(0)
          #          else:
                        #print("No cracks found!!!")
            #            cv2.waitKey(0)
         #       else:
                    #print("No cracks found!!")
        #else:
            #print("No cracks found!")
           # cv2.waitKey(0)
      #  print(area)
       # print(arc)

        #draw contour in empty pics
        #cv2.drawContours(con[i], contours, -1, (0, 255, 0), 3)

        #show pic/contour
        #cv2.imshow("ss", con[i])
    cv2.waitKey(0)
    return (knak)
        # plt.subplot(4, 3, i+1), plt.imshow(hsv[i])
    # plt.show()

    # for i in range(len(hsv)):
    #   for y in range(len(hsv[i][1, :, :])):
    #      for x in range(len(hsv[i][:, 1, :])):
    #         im.append(hsv[i][x, y, :])


    # cv2.imshow("hej", im[1])

    # cv2.waitKey(0)
findcracks("C:/Users/rasmu/Desktop/s/*.jpg")
print(findcracks())
