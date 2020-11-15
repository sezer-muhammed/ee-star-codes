import cv2
import numpy as np
import os
import glob
import pandas as pd
import xml.etree.ElementTree as cET
import random
import xml.etree.cElementTree as ET
import time
size = 300
label_ismi = "sezer"

paths = glob.glob('input/*.jpg')



def yuzVer():
    sayi = random.randint(0, int(len(paths)))
    xmls = paths[sayi].split(".")[0:-1]
    xmls = xmls[0] + ".xml"
    #print(xmls)
    tree = cET.parse(xmls)
    root = tree.getroot()
    for member in root.findall('object'):
        value = (int(member[4][0].text), int(member[4][1].text), int(member[4][2].text), int(member[4][3].text))
    frame = cv2.imread(paths[sayi])
    roi = frame[value[1]:value[3], value[0]:value[2]]
    return (roi, (value[2] - value[0]), (value[3] - value[1]))

fotopaths = glob.glob('foto/*.jpg')
fotopaths = fotopaths * 4

def fotoVer(sira):
    frame = cv2.imread(fotopaths[sira])
    frame = cv2.resize(frame, (300, 300))
    return (frame, 300, 300)

print("Toplamda", len(fotopaths), "fotoğraf var. Başlıyor")
time.sleep(4)


for i in range(0, len(fotopaths)):
    try:
        (foto, fotoX, fotoY) = fotoVer(i)
        (yuz, yuzX, yuzY) = yuzVer()

        koordinatX = fotoX - yuzX
        koordinatY = fotoY - yuzY
        if (i % 100) == 0:
            print(i, "tanesi tamamlandı kalan", len(fotopaths) - i)
        if koordinatX and koordinatY > 0:
            randomX = random.randint(0, koordinatX)
            randomY = random.randint(0, koordinatY)

            foto[randomY:(randomY+yuzY), randomX:(randomX+yuzX)] = yuz
            #cv2.imshow("asd", foto)
            isim = "copied" + str(i)
            fotoisim = isim + ".jpg"
            cv2.imwrite("output/" + fotoisim, foto)
            file = open("output/"+isim+".xml", "w") 
            file.write("<annotation>\n")
            file.write("	<folder>output</folder>\n")
            file.write("	<filename>"+fotoisim+"</filename>\n")
            file.write("	<path>C:/Users/muhammedsezer/Desktop/foto_uret/output/"+fotoisim+"</path>\n")
            file.write("	<source>\n")
            file.write("		<database>Unknown</database>\n")
            file.write("	</source>\n")
            file.write("	<size>\n")
            file.write("		<width>300</width>\n")
            file.write("		<height>300</height>\n")
            file.write("		<depth>3</depth>\n")
            file.write("	</size>\n")
            file.write("	<segmented>0</segmented>\n")
            file.write("	<object>\n")
            file.write("		<name>sezer</name>\n")
            file.write("		<pose>Unspecified</pose>\n")
            file.write("		<truncated>0</truncated>\n")
            file.write("		<difficult>0</difficult>\n")
            file.write("		<bndbox>\n")
            file.write("			<xmin>{}</xmin>\n".format(randomX))
            file.write("			<ymin>{}</ymin>\n".format(randomY))
            file.write("			<xmax>{}</xmax>\n".format(randomX + yuzX))
            file.write("			<ymax>{}</ymax>\n".format(randomY + yuzY))
            file.write("		</bndbox>\n")
            file.write("	</object>\n")
            file.write("</annotation>\n")
            file.close()
            #cv2.waitKey(1)
    except:
        pass