import glob
import pandas as pd
from pathlib import Path
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
import os

def pdToXml(name, coordinates, size,img_folder):
    xml = ['<annotation>']
    xml.append("    <folder>{}</folder>".format(img_folder))
    xml.append("    <filename>{}</filename>".format(name))
    xml.append("    <source>")
    xml.append("        <database>Unknown</database>")
    xml.append("    </source>")
    xml.append("    <size>")
    xml.append("        <width>{}</width>".format(size["width"]))
    xml.append("        <height>{}</height>".format(size["height"]))
    xml.append("        <depth>3</depth>".format())
    xml.append("    </size>")
    xml.append("    <segmented>0</segmented>")

    for field in coordinates:
        xmin, ymin = max(0,field[0]), max(0,field[1])
        xmax = min(size["width"], field[0]+field[2])
        ymax = min(size["height"], field[1]+field[3])

        xml.append("    <object>")
        xml.append("        <name>Face</name>")
        xml.append("        <pose>Unspecified</pose>")
        xml.append("        <truncated>0</truncated>")
        xml.append("        <difficult>0</difficult>")
        xml.append("        <bndbox>")
        xml.append("            <xmin>{}</xmin>".format(int(xmin)))
        xml.append("            <ymin>{}</ymin>".format(int(ymin)))
        xml.append("            <xmax>{}</xmax>".format(int(xmax)))
        xml.append("            <ymax>{}</ymax>".format(int(ymax)))
        xml.append("        </bndbox>")
        xml.append("    </object>")
    xml.append('</annotation>')

    return '\n'.join(xml)



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
    if w <= wmax and h <= hmax:
        w = 2 * (np.sqrt((maxis * np.cos(angle)) ** 2 + (minaxis * np.sin(angle)) ** 2))
        h = 2 * (np.sqrt((maxis * np.sin(angle)) ** 2 + (minaxis * np.cos(angle)) ** 2))
        xmax = xcoor - w / 2
        ymax = ycoor - h / 2
    else:
        w = 0
        h = 0
        xmax = 0
        ymax = 0

    return xmax,ymax,w,h

def saveXMLToFile(name, file):
    with open(name, "w+") as f:
        f.write(file)
def changePandasExtension(row):
    return row.replace(".jpg", ".xml")

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
                #fig, ax = plt.subplots(1)
                #ax.imshow(img)
                (h, w, _) = img.shape
                s = int(arr[i+1])
                nw = []
                for j in range(0, s):
                    coord = arr[i + 2 + j]
                    trans = transformCordinates(coord.split(" "),h,w)
                    nw.append(trans)
                    # print(trans)
                    #newf = patches.Rectangle(
                    #    (trans[0], trans[1]), trans[2], trans[3],
                    #     linewidth=1,
                    #     edgecolor = 'b',
                    #     facecolor ='none')
                    #ax.add_patch(newf)
                #plt.show()

                my_dict["annotation"] = nw
                my_dict["size"] = {"height": h, "width": w}
                arr_temp.append(my_dict)
                #print(arr_temp)

                i = i+1+s
            except:
                print("{}not found...".format(val))
                i+=1
        else:
            i+=1
    print(len(arr_temp))
    return arr_temp


def returnEllipseListFiles(path):
  return [str(f) for f in Path(path).glob("**/*-ellipseList.txt")]


folder = glob.glob("dataset/*.jpg")
folder = pd.Series(folder)
files = returnEllipseListFiles("labels")
arr4 = []
for file in files:
    arr4 += generateArray(file)

df = pd.DataFrame(arr4)
df["xml_name"] = df["name"].apply(changePandasExtension)
df["xml_file"] = df.apply(lambda row: pdToXml(row["name"],row["annotation"], row["size"], "image"),axis=1)
df.apply(lambda row: saveXMLToFile(os.path.join("dataset", row["xml_name"]), row["xml_file"]),axis=1)

names = df["name"].values
folder = folder.apply(lambda x: x.replace("dataset\\",""))
val = folder.isin(names)
print(val)

cool_files = folder[val]
print(cool_files)
val = val.apply(lambda row: not row)

delete_files = folder[val]
delete_files.apply(lambda x: os.remove(os.path.join("dataset", x)))