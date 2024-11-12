import os
import numpy as np
import xml.etree.ElementTree as ET
from PIL import Image

data_dir = './training'
image_dir = os.path.join(data_dir, 'images')
xml_dir = os.path.join(data_dir, 'annotations')
i=0
# Ottieni una lista di nomi di file di immagine
image_files = os.listdir(image_dir)
print(len(image_files))
# Loop sui file di immagine
for image_file in image_files:
    # Carica l'immagine
    image_path = os.path.join(image_dir, image_file)
    image = Image.open(image_path)
    # Converti l'immagine in un array numpy
    image_array = np.array(image)

    # Carica il file XML corrispondente
    xml_file = os.path.splitext(image_file)[0] + '.xml'
    xml_path = os.path.join(xml_dir, xml_file)
    tree = ET.parse(xml_path)
    root = tree.getroot()
    for obj in root.findall('object'):
        i=i+1
        # Estrai le informazioni necessarie dal file XML
        class_name = obj.find('name').text
        xmin = int(obj.find('bndbox/xmin').text)
        ymin = int(obj.find('bndbox/ymin').text)
        xmax = int(obj.find('bndbox/xmax').text)
        ymax = int(obj.find('bndbox/ymax').text)
        if xmax-xmin<200:
            xmin=xmin-int((200-(xmax-xmin))/2)
            xmax=xmax+int((200-(xmax-xmin))/2)
        if ymax-ymin<200:
            ymin=ymin-int((200-(ymax-ymin))/2)
            ymax=ymax+int((200-(ymax-ymin))/2)
        width, height = image.size
        # Fai qualcosa con l'immagine e le informazioni estratte
        #print(f"Immagine {image_file} caricata con la classe {class_name} e il bounding box ({xmin}, {ymin}, {xmax}, {ymax})")
        if xmin>0 or ymin>0 or xmax<width or ymax<height:
            cropped_image = image.crop((xmin, ymin, xmax, ymax))
            cropped_image.save('./'+str(i)+image_file)
