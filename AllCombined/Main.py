import os
import cv2

import root
import Coating
import waterMain
import offset
import mainCracks
import glob
images = [cv2.imread(file) for file in glob.glob("pictures/*.PNG")] + [cv2.imread(file) for file in glob.glob("pictures/*.JPG")]
images = [file for file in glob.glob("pictures/*.PNG")] + [file for file in glob.glob("pictures/*.JPG")]

#print(images)
f = open("resultsWater.txt", "a")

for x in range(len(images)):
    image = cv2.imread(images[x])
    try:
        waterLevel = waterMain.getWater(image)
    except:
        waterLevel = 0
    if waterLevel > 0:
        f.write("\n\nImage - "+images[x])
        f.write("\nRoots: "+str( root.checkForRoots(image)))
        f.write("\nCoating: "+ str(Coating.getCoating(image)))
        try:
            f.write("\nWaterlevel: "+ str(waterMain.getWater(image)))
        except:
            f.write("\nWaterLevel: 0%")
        f.write("\nOffset: "+ str( offset.getOffset(image)))
        f.write("\nCrack: "+ str( mainCracks.findCracks(image)))
        print(images[x])
f.close()
