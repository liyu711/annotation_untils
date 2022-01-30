import tkinter as tk
from tkinter import filedialog as fd
import pandas as pd
import os, glob
from natsort import natsorted, ns

root = tk.Tk()
root.withdraw()

'''!!!!Change dir_prefix!!!!'''
dir_prefix = "E:/DevProjects/CRUW/processed_detections"

## load file sizes of all images
'''!!!!Change imgs_dir!!!!'''
imgs_dir = fd.askdirectory()
imgs_dir = imgs_dir + "/*.jpg"
print(imgs_dir)

img_files = glob.glob(imgs_dir)
img_files = natsorted(img_files, key=lambda y: y.lower())
sizes = []
file_names = []
for img in img_files:
    size = os.path.getsize(img)
    file_names.append(img[-14:]) # FIXME bug might be here
    sizes.append(size)

original_txt_file = fd.askopenfilename()
in_file = open(original_txt_file)
print(original_txt_file)

''' !!!!Change output_name!!!!'''
output_name = dir_prefix + '/2019_04_30_mlms002'
output_txt = output_name + '.txt'
out_file = open(output_txt, 'w')
out_file.write("filename,file_size,file_attributes,region_count,\
region_id,region_shape_attributes,region_attributes\n")
content = in_file.readlines()
print("total number of objects detected in original txt:", len(content))

## line by line process the txt input files of original fields
for i, line in enumerate(content):
    og_fields = list(line.strip().split(' '))
    x1 = int(float(og_fields[4]))
    y1 = int(float(og_fields[5]))
    x2 = int(float(og_fields[6]))
    y2 = int(float(og_fields[7]))
    width = abs(x1 - x2)
    height = abs(y1 - y2)
    class_id = og_fields[2]
    confidence = og_fields[3]
    if width > 17 and height > 20:  # uncomment for filtering out small bounding boxes
        out_file.write("{file_name},{file_size},\"{{}}\",0,0,\"{{\"\"name\"\":\"\"\
rect\"\",\"\"x\"\":{x},\"\"y\"\":{y},\"\"width\"\":{w},\"\"height\"\":{h}}}\",\"{{\"\"class\"\":\"\"{class_name}\"\",\
\"\"conf\"\":\"\"{conf}\"\"}}\"\n". \
                       format(file_name=file_names[int(float(og_fields[0]))], file_size=sizes[int(float(og_fields[0]))],
                              x=x1,
                              y=y1, w=width, h=height, class_name=class_id, conf=confidence))

in_file.close()
out_file.close()

read_file = pd.read_csv(output_txt)

output_csv = output_name + '.csv'  # FIXME changed
read_file.to_csv(output_csv, index=None)
