import numpy as np
import cv2

imgOriginal = cv2.imread('roots_IMG1.jpg',1) # RGB
imgOriginalHSV = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2HSV) # HSV
#blue_channel = imgOriginal[:,:,0] # Blue channel

# Get size of img. Creates a new blank image of the img size
height, width, channels = imgOriginal.shape
blank_image = np.zeros((height,width,3), np.uint8)


# Threshold values for the blue channel
hsv_low = np.array([100, 0, 0])
hsv_high = np.array([255, 255, 255])

# inRange function
#imgThresholded = cv2.inRange(np.float32(blue_channel), thresh_low, thresh_high)
imgHSVthresholded = cv2.inRange(np.float32(imgOriginalHSV), hsv_low, hsv_high)

#edges = cv2.Canny(blue_channel,100,200)

# Creates a morphology kernel of 5x5 size in the shape of an ellipse
kernelEllipse = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))

# Morph close and open
#morphClosedImg = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernelEllipse)
#imgMorphed = cv2.morphologyEx(morphClosedImg, cv2.MORPH_OPEN, kernelEllipse)

# Contours
#contours, hierarchy = cv2.findContours(imgMorphed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(blank_image, contours, -1, (0, 255, 0), 3)

# image resizing
def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):

    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)
#imgOriginal = ResizeWithAspectRatio(imgThresholded , width=420)


# Show pictures
cv2.imshow('img 1', imgHSVthresholded)
cv2.waitKey(0)
cv2.destroyAllWindows()


## Light images are 3, 4, 6, 7
#light roots
#r: 100-230
#g: 100-230
#b: 140-245

## Dark images are 1, 2, 5, 8, 9
#dark roots
#r: 50-110
#g: 70-130
#b: 50-130
