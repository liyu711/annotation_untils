import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def process_dataset(df):
    new_seq_dir = []
    new_frame_id = []
    new_side = []
    match = {
        'images_0': 'l',
        'images_1': 'r'
    }
    for row in df.iterrows():
        pairs = row[1][0]
        left = pairs.split(" ")[0]
        right = pairs.split(" ")[1]
        left_elements = left.split("/")
        right_elements = right.split("/")
        new_seq_dir.append(left_elements[0])
        new_seq_dir.append(right_elements[0])
        new_frame_id.append(int(left_elements[2].replace(".jpg", "")))
        new_frame_id.append(int(right_elements[2].replace(".jpg", "")))
        new_side.append(match[left_elements[1]])
        new_side.append(match[right_elements[1]])
    df_new = pd.DataFrame()
    df_new["seq_dir"] = new_seq_dir
    df_new["frame_id"] = new_frame_id
    df_new["side"] = new_side
    df_new = df_new.sample(frac=1).reset_index(drop=True)
    return df_new

# df_new.to_csv("/mnt/disk1/Yudong/monodepth2/splits/cruw_train/train_files.txt",header=False, index=False, sep=" ")

if __name__ == '__main__':
    old_train_file_path = "/mnt/disk1/Yudong/datasets/training_files.txt"
    df = pd.read_csv(old_train_file_path, header=None)
    train, val = train_test_split(df, test_size=0.2)
    train_processed = process_dataset(train)
    val_processed = process_dataset(val)
    # print(train_processed.__len__())
    # print(val_processed.__len__())
    train_processed.to_csv("/mnt/disk1/Yudong/monodepth2/splits/cruw_train/train_files.txt",header=False, index=False, sep=" ")
    val_processed.to_csv("/mnt/disk1/Yudong/monodepth2/splits/cruw_train/val_files.txt",header=False, index=False, sep=" ")
