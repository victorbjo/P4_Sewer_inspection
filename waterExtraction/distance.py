import cv2
import numpy as np
import math
from matplotlib import pyplot as plt
import lineSearch as lines

def getDis(line, x, y,r):
    print("line"+str(line))
    dX = abs(line[0]-line[2])
    dY = abs(line[1]-line[3])
    a=dY/dX
    b=line[1]+a*line[0]
    print("X,Y:"+str(x)+", "+str( y))
    dist1 = abs(a*-x+b-x)
    dist2 = math.sqrt(a*a+1)
    dist = dist1/dist2
    print("Distance: "+str(dist))
    print("R:"+str(r))
    print("X2:"+str(x*2))
    
    length=((line[2]-line[0])**2)+((line[3]-line[1])**2)
    length=math.sqrt(length)
    print(length)
    print("No")
#def circleArea()
def calcWater(line,x,y,r,crop,start,output):
    b=r
    B=90
    c=((line[2]-line[0])**2)+((line[3]-line[1])**2)
    c=np.sqrt(c)/2 
    C = np.degrees(np.arcsin((np.sin(np.radians(B))*c)/b))
    #C = np.arcsin((sin(90)*c)/r)
    A = 180-B-C
    a = (np.sin(np.radians(A))*b)/np.sin(np.radians(B))
    '''print("line"+str(line))
    print("R: " +str(r))
    print("c: " +str(c))
    print("C: " +str(C))
    print("A: " +str(A))
    print("a: " +str(a))
    print((line[0]+line[2])/2)
    print(x-r)'''
    lineX0 = x-r+line[0]
    lineY0 = y-r+line[1]
    lineX1 = x-r+line[2]
    lineY1 = y-r+line[3]
    X = int(round((lineX0+lineX1)/2))
    Y = int(round((lineY0+lineY1)/2))
    #print((C*2)/360)
    waterArea = 0.5*r**2*(np.radians(C*2)-np.sin(np.radians(C*2)))
    #waterArea = (c*2)/360*(np.pi/4*((r*2)**2))
    #print("Water Area: "+str(waterArea))
    area = np.pi*r**2
    #print("Area: "+str(area))
    #print(waterArea/area*100)
    cv2.line(output,(x,y),(X,Y),(255,200,100),5)
    lines_edges = cv2.addWeighted(output, 0, start, 1, 0)
    #print(waterArea/area*100)
    return(round(waterArea/area*100))




