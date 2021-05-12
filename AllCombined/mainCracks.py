import cv2
import glob
import isolateCrack as isolate
from matplotlib import pyplot as plt
import numpy as np
def findCracks(pic):
    #load images
    #images = [cv2.imread(file) for file in glob.glob("C:/git/P4_Sewer_inspection/Cracks/2/*.jpg")]
    #images = [cv2.imread(file) for file in glob.glob(pic)]
    images = [pic]
    #print(len(images))
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
        #Tjek.append(cv2.inRange(hsv[i], (100, 25, 30), (170, 130, 80)))

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
                if 50 < cv2.contourArea(contours[j]) < 3000:
                    area[j] = cv2.contourArea((contours[j]))
                    arc[j] = cv2.arcLength(contours[j], 1)
                    circularity[j] = (4 * 3.14 * area[j]) / (int(arc[j]) ** 2)
                    #print("circularity: ", circularity)
                    #print("area", area)
                    #print("arc", arc)
                    cv2.drawContours(images[i], contours, j, (0, 255, 0), 1)
                    #cv2.imshow("bin", Tjek[i])
                    cv2.imshow("ss", images[i])
                    knak = 1
                    cv2.waitKey(0)
                # if 350 < cv2.contourArea(contours[j]) < 2000: #800
                #     area.append(cv2.contourArea(contours[j]))
                #     if cv2.arcLength(contours[j], True) < 2000: #200
                #         arc.append(cv2.arcLength(contours[j], True))
                #         # draw contour in empty pics
                #         cv2.drawContours(images[i], contours, j, (0, 255, 0), 1)
                #         #print("AHH SHIET")
                #
                #         # print(circularity[j])
                #         # print(area)
                #         # print(arc)
                #         cv2.imshow("ss", images[i])
                #         knak = 1
                #
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

# pics = []
# pics = [cv2.imread(file) for file in glob.glob("f:/Crack/*.jpg")]
# for t in range (len(pics)):
#     #print(t+1)
#     pic = pics[t]
#     findCracks(pic)



        # plt.subplot(4, 3, i+1), plt.imshow(hsv[i])
    # plt.show()

    # for i in range(len(hsv)):
    #   for y in range(len(hsv[i][1, :, :])):
    #      for x in range(len(hsv[i][:, 1, :])):
    #         im.append(hsv[i][x, y, :])


    # cv2.imshow("hej", im[1])

    # cv2.waitKey(0)
