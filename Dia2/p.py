import glob
import pandas as pd
from pathlib import Path
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
import os



def transformCordinates(coordinates, wmax, hmax):
    maxis = coordinates[0]
    minaxis = coordinates[1]
    angle = coordinates[2]
    xcoor = coordinates[3]
    ycoor = coordinates[4]

    maxis = float(maxis)
    minaxis = float(minaxis)
    angle = float(angle)
    xcoor = float(xcoor)
    ycoor = float(ycoor)
    w = 2*(np.sqrt((maxis*np.cos(angle))**2 + (minaxis*np.sin(angle))**2))
    h = 2*(np.sqrt((maxis*np.sin(angle))**2 + (minaxis*np.cos(angle))**2))
    xmax = xcoor-w/2
    ymax = ycoor-h/2

    return(xmax,ymax,w,h)


def generateArray(file):
    with open(file, "r") as f:
        arr = f.read().splitlines()

    arr_len = len(arr)
    i = 0
    rg = re.compile("(\d)*_(\d)*_(\d)*_big")
    arr_temp = []
    while i != arr_len:
        val = arr[i]

        mtch = rg.match(val)
        if mtch:
            try:
                my_dict = dict()
                val = "{}.jpg".format(val)

                my_dict["name"] = val

                #matplotlib
                img = mpimg.imread(os.path.join("dataset", val))
                fig, ax = plt.subplots(1)
                ax.imshow(img)
                (h, w, _) = img.shape
                s = int(arr[i+1])

                for j in range(0, s):
                    coord = arr[i + 2 + j]
                    trans = transformCordinates(coord.split(" "),h,w)
                    # print(trans)
                    #print(trans)
                    newf = patches.Rectangle(
                        (trans[0], trans[1]), trans[2], trans[3],
                         linewidth=1,
                         edgecolor = 'b',
                         facecolor ='none')
                    ax.add_patch(newf)
                plt.show()

                my_dict["annotations"] = arr_temp

                i = i+1+s
            except:
                print("{}not found...".format(val))
                i+=1
        else:
            i+=1


def returnEllipseListFiles(path):
  return [ str(f) for f in Path(path).glob("**/*-ellipseList.txt") ]


folder = glob.glob("dataset/*.jpg")
folder = pd.Series(folder)
files = returnEllipseListFiles("labels")

print(folder)
print(files)

d = generateArray(files[0])

print(d)











