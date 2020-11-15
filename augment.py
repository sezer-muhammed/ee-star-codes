import cv2
import numpy as np
import os
import glob
import pandas as pd
import xml.etree.ElementTree as cET
import random
import xml.etree.cElementTree as ET
mozaik = 1
parlat = 1.2
boyut = 1.1

size = 300

def labelOlustur(fotoismi, solUstXmin, solUstYmin, solUstXmax, solUstYmax, sagUstXmin, sagUstYmin, sagUstXmax, sagUstYmax, solAltXmin, solAltYmin, solAltXmax, solAltYmax, sagAltXmin, sagAltYmin, sagAltXmax, sagAltYmax):

  solUstXmin = int(solUstXmin/2)
  solUstYmin = int(solUstYmin/2)
  solUstXmax = int(solUstXmax/2)
  solUstYmax = int(solUstYmax/2)

  sagUstXmin = int(sagUstXmin/2) + 150
  sagUstYmin = int(sagUstYmin/2)
  sagUstXmax = int(sagUstXmax/2) + 150
  sagUstYmax = int(sagUstYmax/2)

  solAltXmin = int(solAltXmin/2)
  solAltYmin = int(solAltYmin/2) + 150
  solAltXmax = int(solAltXmax/2)
  solAltYmax = int(solAltYmax/2) + 150

  sagAltXmin = int(sagAltXmin/2) + 150
  sagAltYmin = int(sagAltYmin/2) + 150
  sagAltXmax = int(sagAltXmax/2) + 150
  sagAltYmax = int(sagAltYmax/2) + 150

  annotation = ET.Element("annotation")
  m1 = ET.SubElement(annotation, "folder")
  
  
  m1.text = "input"
  
  m2 = ET.SubElement(annotation, "filename")
  
  m2.text = fotoismi
  
  m3 = ET.SubElement(annotation,"path")
  m3.text = "C:\\Users\\muhammedsezer\\Desktop\\augment\\output\\" + fotoismi

  m4 = ET.SubElement(annotation,"source")
  m41 = ET.SubElement(m4,"database")
  m41.text = "Unknown"

  m5 = ET.SubElement(annotation,"size")
  m51 = ET.SubElement(m5,"width")
  m51.text = "300"
  m52 = ET.SubElement(m5,"height")
  m52.text = "300"
  m53 = ET.SubElement(m5,"depth")
  m53.text = "3"

  m6 = ET.SubElement(annotation,"segmented")
  m6.text = "0"

  m7 = ET.SubElement(annotation,"object")
  m71 = ET.SubElement(m7,"name")
  m71.text = "bag"
  m72 = ET.SubElement(m7,"pose")
  m72.text = "Unspecified"
  m73 = ET.SubElement(m7,"truncated")
  m73.text = "0"
  m74 = ET.SubElement(m7,"difficult")
  m74.text = "0"
  m75 = ET.SubElement(m7,"bndbox")
  m751 = ET.SubElement(m75,"xmin")
  m751.text = str(sagUstXmin)
  m752 = ET.SubElement(m75,"ymin")
  m752.text = str(sagUstYmin)
  m753 = ET.SubElement(m75,"xmax")
  m753.text = str(sagUstXmax)
  m754 = ET.SubElement(m75,"ymax")
  m754.text = str(sagUstYmax)

  m8 = ET.SubElement(annotation,"object")
  m81 = ET.SubElement(m8,"name")
  m81.text = "bag"
  m82 = ET.SubElement(m8,"pose")
  m82.text = "Unspecified"
  m83 = ET.SubElement(m8,"truncated")
  m83.text = "0"
  m84 = ET.SubElement(m8,"difficult")
  m84.text = "0"
  m85 = ET.SubElement(m8,"bndbox")
  m851 = ET.SubElement(m85,"xmin")
  m851.text = str(solAltXmin)
  m852 = ET.SubElement(m85,"ymin")
  m852.text = str(solAltYmin)
  m853 = ET.SubElement(m85,"xmax")
  m853.text = str(solAltXmax)
  m854 = ET.SubElement(m85,"ymax")
  m854.text = str(solAltYmax)

  m9 = ET.SubElement(annotation,"object")
  m91 = ET.SubElement(m9,"name")
  m91.text = "bag"
  m92 = ET.SubElement(m9,"pose")
  m92.text = "Unspecified"
  m93 = ET.SubElement(m9,"truncated")
  m93.text = "0"
  m94 = ET.SubElement(m9,"difficult")
  m94.text = "0"
  m95 = ET.SubElement(m9,"bndbox")
  m951 = ET.SubElement(m95,"xmin")
  m951.text = str(solUstXmin)
  m952 = ET.SubElement(m95,"ymin")
  m952.text = str(solUstYmin)
  m953 = ET.SubElement(m95,"xmax")
  m953.text = str(solUstXmax)
  m954 = ET.SubElement(m95,"ymax")
  m954.text = str(solUstYmax)

  m10 = ET.SubElement(annotation,"object")
  m101 = ET.SubElement(m10,"name")
  m101.text = "bag"
  m102 = ET.SubElement(m10,"pose")
  m102.text = "Unspecified"
  m103 = ET.SubElement(m10,"truncated")
  m103.text = "0"
  m104 = ET.SubElement(m10,"difficult")
  m104.text = "0"
  m105 = ET.SubElement(m10,"bndbox")
  m1051 = ET.SubElement(m105,"xmin")
  m1051.text = str(sagAltXmin)
  m1052 = ET.SubElement(m105,"ymin")
  m1052.text = str(sagAltYmin)
  m1053 = ET.SubElement(m105,"xmax")
  m1053.text = str(sagAltXmax)
  m1054 = ET.SubElement(m105,"ymax")
  m1054.text = str(sagAltYmax)
  
  


  tree = ET.ElementTree(annotation)
  tree.write("output/" + fotoismi.split(".")[0] +".xml")

def xml_to_csv(path):
	xml_list = []
	sayac = 0
	fotono = 0
	xmls = glob.glob(path + '/*.xml')
	xmls = xmls * 6
	random.shuffle(xmls)
	frame = np.zeros((300, 300, 3), np.uint8)
	for xml_file in xmls:
		imgpath = "input/" + xml_file.split("\\")[-1].split(".")[0] + ".jpg"
		img = cv2.imread(imgpath)
		img = cv2.resize(img, (150, 150))

		if sayac == 0:
			frame[0:150, 0:150] = img
		if sayac == 1:
			frame[0:150, 150:300] = img
		if sayac == 2:
			frame[150: 300, 0:150] = img
		if sayac == 3:
			frame[150:300, 150:300] = img
		tree = cET.parse(xml_file)
		root = tree.getroot()
		for member in root.findall('object'):
			value = (int(member[4][0].text),
					 int(member[4][1].text),
					 int(member[4][2].text),
					 int(member[4][3].text)
					 )
			#print(imgpath, value, sayac)
			xml_list.append(value)
			sayac = sayac + 1

		if sayac == 4:
			sayac = 0
			fotoisim = "mixed" + str(fotono) + ".jpg"
			labelOlustur(fotoisim,  xml_list[0][0], xml_list[0][1], xml_list[0][2], xml_list[0][3], xml_list[1][0], xml_list[1][1], xml_list[1][2], xml_list[1][3], xml_list[2][0], xml_list[2][1], xml_list[2][2], xml_list[2][3], xml_list[3][0], xml_list[3][1], xml_list[3][2], xml_list[3][3])
			cv2.imwrite("output/" + fotoisim, frame)
			fotono = fotono + 1
			if fotono % 100 == 0:
				print(fotono)
			xml_list = []
	return 1


def main():
	for folder in ['input']:
		image_path = os.path.join(os.getcwd(), (folder))
		xml_df = xml_to_csv(image_path)
        #print(xml_df)


main()
