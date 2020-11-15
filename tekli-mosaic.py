import cv2
import numpy as np
import os
import glob
import pandas as pd
import xml.etree.ElementTree as cET
import random
import xml.etree.cElementTree as ET

harici_path = glob.glob('haric/*.jpg')
labeled_path = glob.glob('input/*.jpg')
labeled_path = labeled_path * 2

size = 300

def koordinatVer(path):
	tree = cET.parse(path)
	root = tree.getroot()
	for member in root.findall('object'):
		value = (int(member[4][0].text),int(member[4][1].text),int(member[4][2].text),int(member[4][3].text))
	return value

def fotoVer(xml_path, foto_path):
	random_bir = random.randint(0, len(harici_path))
	random_iki =random.randint(0, len(harici_path))
	random_uc = random.randint(0, len(harici_path))
	koord = koordinatVer(xml_path)
	reel_foto = cv2.imread(foto_path)
	hrc_foto_bir = cv2.imread(harici_path[random_bir])
	hrc_foto_iki = cv2.imread(harici_path[random_iki])
	hrc_foto_uc = cv2.imread(harici_path[random_uc])
	reel_foto = cv2.resize(reel_foto, (150, 150))
	hrc_foto_bir = cv2.resize(hrc_foto_bir, (150, 150))
	hrc_foto_iki = cv2.resize(hrc_foto_iki, (150, 150))
	hrc_foto_uc = cv2.resize(hrc_foto_uc, (150, 150))
	return (koord, reel_foto, hrc_foto_bir, hrc_foto_iki, hrc_foto_uc)

def fotoOlustur(xmin, ymin, xmax, ymax, reel_foto, hrc1, hrc2, hrc3):
	konumX = random.randint(0, 1)
	konumY = random.randint(0, 1)

	xmin = int(xmin/2 + (konumX * 150))
	xmax = int(xmax/2 + (konumX * 150))
	ymin = int(ymin/2 + (konumY * 150))
	ymax = int(ymax/2 + (konumY * 150))

	frame = np.zeros((300, 300, 3), np.uint8)

	frame[((konumY)*150):((konumY+1)*150), ((konumX)*150):((konumX+1)*150)] = reel_foto
	frame[((1-konumY)*150):(((1-konumY)+1)*150), ((konumX)*150):((konumX+1)*150)] = hrc1
	frame[((konumY)*150):((konumY+1)*150), ((1-konumX)*150):(((1-konumX)+1)*150)] = hrc2
	frame[((1-konumY)*150):(((1-konumY)+1)*150), ((1-konumX)*150):(((1-konumX)+1)*150)] = hrc3
	return ((xmin, ymin, xmax, ymax), frame)

def kaydet(koord, frame, sayac):
	isim = "hrc-mosaic" + str(sayac)
	foto = "hrc-mosaic" + str(sayac) + ".jpg"
	cv2.imwrite(("output/" + foto), frame)
	file = open("output/"+isim+".xml", "w") 
	file.write("<annotation>\n")
	file.write("	<folder>output</folder>\n")
	file.write("	<filename>"+foto+"</filename>\n")
	file.write("	<path>C:/Users/muhammedsezer/Desktop/augment/output/"+foto+"</path>\n")
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
	file.write("		<name>bag</name>\n")
	file.write("		<pose>Unspecified</pose>\n")
	file.write("		<truncated>0</truncated>\n")
	file.write("		<difficult>0</difficult>\n")
	file.write("		<bndbox>\n")
	file.write("			<xmin>{}</xmin>\n".format(koord[0]))
	file.write("			<ymin>{}</ymin>\n".format(koord[1]))
	file.write("			<xmax>{}</xmax>\n".format(koord[2]))
	file.write("			<ymax>{}</ymax>\n".format(koord[3]))
	file.write("		</bndbox>\n")
	file.write("	</object>\n")
	file.write("</annotation>\n")
	file.close()

sayac = 0

for i in (labeled_path):
	try:
		base_path = i.split(".")[0]
		xml_path = base_path + ".xml"
		koord, reel_foto, hrc1, hrc2, hrc3 = fotoVer(xml_path, i)
		koord, yeni_foto = fotoOlustur(koord[0], koord[1], koord[2], koord[3], reel_foto, hrc1, hrc2, hrc3)
		kaydet(koord, yeni_foto, sayac)
		sayac = sayac + 1
	except:
		print("hata!!!")


	
