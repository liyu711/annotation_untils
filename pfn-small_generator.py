import os
import random
import pandas as pd

data_dir = "/mnt/disk1/Yudong/CRUW_SMALL"
sequece_dir = "2019_09_29_onrd0012"
output_dir = "/mnt/disk1/Yudong/datasets/custom_pfn/test_sequence.txt"
left_path = "images_0"
right_path = "images_1"

left_dir = os.path.join(sequece_dir, left_path)
right_dir = os.path.join(sequece_dir, right_path)
image_names = os.listdir(os.path.join(data_dir, left_dir))
image_names.sort()
left = []
right = []
for image in image_names:
    left.append(os.path.join(sequece_dir, left_path, image))
    right.append(os.path.join(sequece_dir, right_path, image))
df = pd.DataFrame(columns=["left_image", "right_image"])
df["left_image"] = left
df["right_image"] = right
df.to_csv(output_dir, header=False, index=False, sep=" ")
