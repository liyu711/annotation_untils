import os.path

import pandas as pd
import numpy as np

def process_sequence(labels_dir, output_dir, smoke):
    print(labels_dir)
    # labels_dir = '/mnt/disk1/Yudong/optimized_bb/2019_09_29_ONRD001_filtered_car_only_.txt'
    output_name = labels_dir.split('/')[-1]
    df = pd.read_csv(labels_dir, sep=' ', header=None)
    df_result = pd.DataFrame()
    classes = np.zeros(df.shape[0]).astype(int)
    x_y_z = (np.zeros(df.shape[0]) - 1).astype(int)
    if smoke:
        df_result['frame_id'] = df[0]
        df_result['class'] = classes
        df_result['left'] = df[17]
        df_result['top'] = df[18]
        df_result['width'] = abs(df[17] - df[19])
        df_result['height'] = abs(df[18] - df[20])
        df_result['conf'] = df[24]
        df_result['x'] = x_y_z
        df_result['y'] = x_y_z
        df_result['z'] = x_y_z
    else:
        df_result['frame_id'] = df[0]
        df_result['class'] = classes
        df_result['left'] = df[4]
        df_result['top'] = df[5]
        df_result['width'] = abs(df[4] - df[6])
        df_result['height'] = abs(df[5] - df[7])
        df_result['conf'] = df[3]
        df_result['x'] = x_y_z
        df_result['y'] = x_y_z
        df_result['z'] = x_y_z
    output_dir = os.path.join(output_dir, output_name)
    df_result.to_csv(output_dir, sep=',', index=False, header=False)

if __name__ == '__main__':
    output_dir = '/mnt/disk1/Yudong/datasets/cruw_test_mot_label'
    base_detection_path = '/mnt/disk1/Yudong/datasets/test_sequence_detections_raw'
    txts = os.listdir(base_detection_path)
    for txt in txts:
        labels_dir = os.path.join(base_detection_path, txt)
        process_sequence(labels_dir, output_dir, False)
