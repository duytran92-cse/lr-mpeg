import matplotlib.pyplot as plt
import os
import numpy as np
import glob

import time

import math

from PIL import Image

### Question 1 >>> Begin
def batch_processing(prefix,ext,indstart,indend):
    pathDB ="./cars//"
    imList=[]
    imProcessed=[]
    Abs_path=os.path.dirname(pathDB)

    if(os.path.exists(Abs_path)):
        imfile_start= prefix+"%02d" %indstart+'.'+ext
        pathStart=os.path.join(Abs_path, imfile_start)
        print("Starting image file:", pathStart)

        imfile_end=prefix+"%02d" %indend+'.'+ext
        pathEnd=os.path.join(Abs_path, imfile_end)
        print("Ending image file", pathEnd)

        #Loading
        tic = time.time()
        print("Loading sequence......")
	## charger tous les images dans imList
        for i in range(indstart, indend + 1):
            imfile = prefix + "%02d" % i + '.' + ext
            path = os.path.join(Abs_path, imfile)
            img = plt.imread(path)
            imList.append(img)
        toc = time.time()
        print(toc-tic, "sec elapsed for loading!")


        tic = time.time()
        print("Processing sequence.....")

        toc = time.time()
        print(toc-tic, "sec elapsed for processing!")
    else:
        print("This path does not exist")
    return imList,imProcessed


## charger tous les images dans imList
pathDB = "./cars//"     # dans Windows, changer "/" par "\"
prefix = "cars_"
indstart = 1
indend = 6
ext = "pgm"

Abs_path=os.path.dirname(pathDB)

imList = []

for ind in range(indstart, indend+1):
    if (os.path.exists(Abs_path)):
        imfile_start= prefix +"%02d" %ind + '.'+ ext
        pathStart=os.path.join(Abs_path,imfile_start)
        print("Starting image file:", str(pathStart))#cars\cars_00.pgm
        imList.append(np.double(Image.open(pathStart)))

print(imList)


### load image by using batch_processing
a,b = batch_processing("cars_", "pgm", 1, 6)


for x in range(0,len(a)):
    plt.subplot(3,2, x+1)
    plt.imshow(a[x], cmap='gray')

plt.show()
### End Question 1

### Question 2 >>> Begin

img = imList[2]     # >>> can change 1,2,3,4,5
def calculDiff(img2):
    tailleMB = 0
    sommeDiff = []#contient le x,y du bloc qui differe le plus.
    
    for x in range(0,int(img.shape[0]/16)*16,16):
        for y in range(0,int(img.shape[1]/16)*16,16):
            #inutile car ce sont des multiples de 16
            tailleMBX = min(img.shape[0]-x, 16)
            tailleMBY = min(img.shape[1]-y, 16)
            #print(tailleMBX, tailleMBY)
            mb = img[x:x+tailleMBX,y:y+tailleMBY]
            mb2 = img2[x:x+tailleMBX,y:y+tailleMBY]
            #calcul de la liste des fenetres a tester :
            maxX = 0
            maxY = 0
            mini = 100000000000000000000
            for xf in range(max(x-tailleMBX,0), min(x+tailleMBX,img.shape[0]-16)):
                for yf in range(max(y-tailleMBY,0), min(y+tailleMBY,img.shape[1]-16)):
                    diff = sum( sum( (mb - img2[xf:xf+tailleMBX,yf:yf+tailleMBY])**2 ) )
                    if(diff < mini):
                        maxX = xf
                        maxY = yf
                        mini = diff
            sommeDiff.append([x, y, maxX, maxY, mini])
    return sommeDiff

for rang in range(len(imList)):
    sommeDiff = calculDiff(imList[rang])
    plt.subplot(3, 2, rang+1)
    for elt in sommeDiff:
        if(elt[0] != elt[2] or elt[1] != elt[3]):
            norm = math.sqrt((elt[2]-elt[0])**2 + (elt[3]-elt[1])**2)
            plt.quiver(elt[1], 352-elt[0],  elt[3]-elt[1] * norm, elt[2]-elt[0] *norm, angles='xy') 
plt.show()

# end question 2
