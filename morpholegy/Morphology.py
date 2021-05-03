import cv2
import numpy as np
from matplotlib import pyplot as plt

def erode(img, k_x, k_y, k_type):
    print(k_x, k_x/2, int(k_x/2))
    
    image = np.zeros(img.shape)
    image.fill(255)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            counter = 0
            if img[x][y] == 0:
                image[x][y] = 0
            else:
                counter = 0
                for i in range(int(k_x/2+1)):
                    for j in range(int(k_y/2+1)):
                        try:
                            if k_type == "rect":
                                if img[x-i][y-j] == 0:
                                    image[x][y] = 0
                                elif img[x-i][y+j] == 0:
                                    image[x][y] = 0
                                elif img[x+i][y-j] == 0:
                                    image[x][y] = 0
                                elif img[x+i][y+j] == 0:
                                    image[x][y] = 0
                            elif k_type == "eclipse":
                                a = 0 
                            elif k_type == "cross":
                                if img[x-i][y] == 0:
                                    image[x][y] = 0
                                elif img[x][y+j] == 0:
                                    image[x][y] = 0
                                elif img[x][y-j] == 0:
                                    image[x][y] = 0
                                elif img[x+i][y] == 0:
                                    image[x][y] = 0
                        except:
                            a=0 #does nothing try except is used so program doesnt crash when kernal is outside of image
               # print(counter)
    return image




def dilate(img, k_x, k_y, k_type):
    print(k_x, k_x/2, int(k_x/2))
    
    image = np.zeros(img.shape)
    
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if img[x][y] == 255:
                image[x][y] = 255
            else:
                for i in range(int(k_x/2+1)):
                    for j in range(int(k_y/2+1)):
                        try:
                            if k_type == "rect":
                                if img[x-i][y-j] == 255:
                                    image[x][y] = 255
                                elif img[x-i][y+j] == 255:
                                    image[x][y] = 255
                                elif img[x+i][y-j] == 255:
                                    image[x][y] = 255
                                elif img[x+i][y+j] == 255:
                                    image[x][y] = 255
                            elif k_type == "eclipse":
                                a = 0 
                            elif k_type == "cross":
                                if img[x-i][y] == 255:
                                    image[x][y] = 255
                                elif img[x][y+j] == 255:
                                    image[x][y] = 255
                                elif img[x][y-j] == 255:
                                    image[x][y] = 255
                                elif img[x+i][y] == 255:
                                    image[x][y] = 255
                        except:
                            a=0 #does nothing try except is used so program doesnt crash when kernal is outside of image
               # print(counter)
    return image


def morphol0gy(img, type, k_x, k_y, k_type):

    if type == "erode":
        image = erode(img, k_x, k_y, k_type)
        return image

    elif type == "dilate":
        image = dilate(img, k_x, k_y, k_type)
        return image

    elif type == "close":
        image1 = dilate(img, k_x, k_y, k_type)
        image2 = erode(image1, k_x, k_y, k_type)
        return image2

    elif type == "open":
        image1 = erode(img, k_x, k_y, k_type)
        image2 = dilate(image1, k_x, k_y, k_type)
        return image2

image = cv2.imread("3_coating.PNG")

thresh = cv2.inRange(image, (100,20,0), (140,255,255))

img = morphol0gy(thresh, "close", 5,5,"rect")
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
test = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
print(img.shape)
cv2.imshow("threshold", thresh)
cv2.imshow("morph me", img)
cv2.imshow("morph cv", test)


