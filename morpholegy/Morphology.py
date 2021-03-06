import cv2
import numpy as np
from matplotlib import pyplot as plt

def erode(img, k_x, k_y, k_type):
    
    image = np.zeros(img.shape) # create new image to store morphology image in
    image.fill(255) # fill image with white

    #loop thorugh every pixel in the original image
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):

            #check if the pixel value is 0
            if img[x][y] == 0:
                image[x][y] = 0
            else:
                # loop through kernal around specific pixel
                for i in range(int(k_x/2+1)):
                    for j in range(int(k_y/2+1)):

                        #try is used to avoid crash when kernal is outside image
                        try:
                            if k_type == "rect": # check for zeros with rectangle kernal
                                if img[x-i][y-j] == 0:
                                    image[x][y] = 0
                                elif img[x-i][y+j] == 0:
                                    image[x][y] = 0
                                elif img[x+i][y-j] == 0:
                                    image[x][y] = 0
                                elif img[x+i][y+j] == 0:
                                    image[x][y] = 0
                            elif k_type == "eclipse": # check for zeros with eclipse kernal
                                    
                                if img[x-i+1][y-j+1] == 0:
                                    image[x][y] = 0
                                elif img[x-i+1][y+j-1] == 0:
                                    image[x][y] = 0
                                elif img[x+i-1][y-j+1] == 0:
                                    image[x][y] = 0
                                elif img[x+i-1][y+j-1] == 0:
                                    image[x][y] = 0

                                elif img[x-1][y-int(k_y/2)] == 0:
                                    image[x][y] = 0
                                elif img[x][y-int(k_y/2)] == 0:
                                    image[x][y] = 0
                                elif img[x+1][y-int(k_y/2)] == 0:
                                    image[x][y] = 0

                                elif img[x-1][y+int(k_y/2)] == 0:
                                    image[x][y] = 0
                                elif img[x][y+int(k_y/2)] == 0:
                                    image[x][y] = 0
                                elif img[x+1][y+int(k_y/2)] == 0:
                                    image[x][y] = 0
                          
                                    
                                elif img[x-int(k_x/2)][y] == 0:
                                    image[x][y] = 0
                                elif img[x+int(k_x/2)][y] == 0:
                                    image[x][y] = 0
                                
                            elif k_type == "cross": # check for zeros with cross kernal
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
    return image




def dilate(img, k_x, k_y, k_type): #works excalty like erode, but instead of checking for zeros in kernal checks for 255 aka white, and the new image is not filled with white
    
    image = np.zeros(img.shape)
    counter = 0
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
                                    
                                if img[x-i+1][y-j+1] == 255:
                                    image[x][y] = 255
                                elif img[x-i+1][y+j-1] == 255:
                                    image[x][y] = 255
                                elif img[x+i-1][y-j+1] == 255:
                                    image[x][y] = 255
                                elif img[x+i-1][y+j-1] == 255:
                                    image[x][y] = 255

                                elif img[x-1][y-int(k_y/2)] == 255:
                                    image[x][y] = 255
                                elif img[x][y-int(k_y/2)] == 255:
                                    image[x][y] = 255
                                elif img[x+1][y-int(k_y/2)] == 255:
                                    image[x][y] = 255

                                elif img[x-1][y+int(k_y/2)] == 255:
                                    image[x][y] = 255
                                elif img[x][y+int(k_y/2)] == 255:
                                    image[x][y] = 255
                                elif img[x+1][y+int(k_y/2)] == 255:
                                    image[x][y] = 255
                          
                                    
                                elif img[x-int(k_x/2)][y] == 255:
                                    image[x][y] = 255
                                elif img[x+int(k_x/2)][y] == 255:
                                    image[x][y] = 255
                                    
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

# below is code used for testing morphology functions:

#image = cv2.imread("3_coating.PNG")
#thresh = cv2.inRange(image, (100,20,0), (140,255,255))

#img = morphol0gy(thresh, "dilate", 5,5,"rect")
#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
#print(kernel)
#test = cv2.morphologyEx(thresh, cv2.MORPH_ERODE, kernel)
#print(img.shape)
#cv2.imshow("threshold", thresh)
#cv2.imshow("threshold", thresh)
#cv2.imshow("morph me", img)
#cv2.imshow("morph cv", test)


