import os
import cv2

import root
import Coating
import waterMain
import offset
import mainCracks

image = cv2.imread("water0.jpg")
root.checkForRoots(image)
print(Coating.getCoating(image))
print(waterMain.getWater(image))
print(offset.getOffset(image))
print(mainCracks.findCracks(image))
