import pandas as pd
import numpy as np
import os

def process_sequence(anno_dir, output_dir):
    anno_table = pd.read_csv(anno_dir, header=None,index_col=None)
# <frame>, <id>, <bb_left>, <bb_top>, <bb_width>, <bb_height>, <conf>, <x>, <y>, <z>
    anno_table = anno_table.rename({0: 'frame_id', 1: 'track_id', 2: 'bb_x', 3: 'bb_y',
                                    4: 'bb_w', 5: 'bb_h', 6: 'conf', 7:'x', 8: 'y', 9:'z'},axis=1)
    # print(anno_table.columns)
    anno_table['bb_x'] = anno_table['bb_x'] + anno_table['bb_w']/2
    anno_table['bb_y'] = anno_table['bb_y'] - anno_table['bb_h']/2
    frames = anno_table['frame_id'].unique()
    class_col = np.zeros(len(anno_table['frame_id'])) + 1
    anno_table['class'] = class_col
    new_columns = ['frame_id', 'class', 'track_id', 'bb_x', 'bb_y', 'bb_w', 'bb_h', 'conf', 'x', 'y', 'z']
    anno_table = anno_table[new_columns]
    for frame in frames:
        output_name = str(frame).zfill(6) + '.txt'
        write_dir = os.path.join(output_dir, output_name)
        bbs_df = anno_table.loc[anno_table['frame_id']==frame]
        bbs_df = bbs_df.drop(['frame_id', 'track_id', 'conf', 'x', 'y', 'z'], axis=1)
        file = open(write_dir, 'w+')
        bbs_df.to_csv(file, header=False, index=False)

def process_mot(mot_dataset_dir):
    train = os.path.join(mot_dataset_dir, 'train')
    test = os.path.join(mot_dataset_dir, 'test')
    train_seqs = os.listdir(train)
    test_seqs = os.listdir(test)
    for seq in test_seqs:
        det_path = os.path.join(test, seq, 'det/det.txt')
        yolo_output = os.path.join(test, seq, 'det/yolo')
        if not os.path.exists(yolo_output):
            os.makedirs(yolo_output)
        process_sequence(det_path, yolo_output)
    for seq in train_seqs:
        det_path = os.path.join(train, seq, 'det/det.txt')
        yolo_output = os.path.join(train, seq, 'det/yolo')
        if not os.path.exists(yolo_output):
            os.makedirs(yolo_output)
        process_sequence(det_path, yolo_output)

def reorganizing_dirs(mot_dir):
    test = os.path.join(mot_dir, 'test')
    train = os.path.join(mot_dir, 'train')
    train_seqs = os.listdir(train)
    test_seqs = os.listdir(test)
    for seq in test_seqs:
        print('processing ' + seq)
        source = os.path.join(test, seq, 'det/yolo')
        dest = os.path.join(test, seq, 'labels')
        print('moved files to '+dest)
        os.rename(source, dest)
        image_dir = os.path.join(test, seq, 'img1')
        image_rename = os.path.join(test, seq, 'images')
        print('Renamed image folder to ' + image_rename)
        os.rename(image_dir, image_rename)
    for seq in train_seqs:
        print('processing ' + seq)
        source = os.path.join(train, seq, 'det/yolo')
        dest = os.path.join(train, seq, 'labels')
        print('moved files to ' + dest)
        os.rename(source, dest)
        image_dir = os.path.join(train, seq, 'img1')
        image_rename = os.path.join(train, seq, 'images')
        print('Renamed image folder to ' + image_rename)
        os.rename(image_dir, image_rename)




if __name__ == '__main__':
    test_sequence = '/mnt/disk1/Yudong/MOT20/train/MOT20-01/det/det.txt'
    test_output_dir = '/mnt/disk1/Yudong/MOT20/train/MOT20-01/det/yolo/'
    mot_dir = '/mnt/disk1/Yudong/MOT20'
    test_source = '/mnt/disk1/Yudong/MOT20/test/MOT20-04/labels'
    test_dest = '/mnt/disk1/Yudong/MOT20/test/MOT20-04/det/labels'
    # process_mot(mot_dir)
    reorganizing_dirs(mot_dir)
    # process_sequence(test_sequence, test_output_dir)
