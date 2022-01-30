import os
import random
import pandas as pd

data_dir = "/mnt/disk1/Yudong/datasets/cruw_stereo_training"
output_dir = "/mnt/disk1/Yudong/datasets/cruw_stereo_training/training_files.txt"
seqs = os.listdir(data_dir)
left_path = "images_0"
right_path = "images_1"
left = []
right = []
for seq in seqs:
    seq_dir = os.path.join(data_dir, seq)
    left_dir = os.path.join(seq_dir, left_path)
    right_dir = os.path.join(seq_dir, right_path)
    images = os.listdir(left_dir)
    random.shuffle(images)
    for image in images:
        left_image_dir = os.path.join(seq, left_path, image)
        right_image_dir = os.path.join(seq, right_path, image)
        left.append(left_image_dir)
        right.append(right_image_dir)
df = pd.DataFrame()
df["left_image"] = left
df["right_image"] = right
df.to_csv(output_dir, index=False, header=False, sep=" ")