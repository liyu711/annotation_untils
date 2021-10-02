import os

import random
from shutil import copyfile

def load_data(collection_dir, is_train, output_dir):
    seqs = os.listdir(collection_dir)
    img_all = []
    leb_all = []
    matches = {}
    for seq in seqs:
        print(seq)
        seq_dir = os.path.join(collection_dir, seq)
        img_folder = os.path.join(seq_dir, 'images')
        images = sorted(os.listdir(img_folder))
        for img in images:
            singe_image_path = os.path.join(img_folder, img)
            img_all.append(singe_image_path)
        label_folder = os.path.join(seq_dir, 'labels')
        labels = sorted(os.listdir(label_folder))
        for label in labels:
            single_label_path = os.path.join(label_folder, label)
            leb_all.append(single_label_path)
    for i in range(len(img_all)):
        matches[img_all[i]] = leb_all[i]
    list_of_items = list(matches.keys())
    print(len(list_of_items))
    random.shuffle(list_of_items)
    output_image_dir = os.path.join(output_dir, 'images')
    output_label_dir = os.path.join(output_dir, 'labels')
    if is_train:
        output_image_dir_train = os.path.join(output_image_dir, 'train')
        output_label_dir_train = os.path.join(output_label_dir, 'train')
        output_image_dir_val = os.path.join(output_image_dir, 'val')
        output_label_dir_val = os.path.join(output_label_dir, 'val')

        train_dict = list_of_items[:int(len(list_of_items) * 0.8)]
        val_dict = list_of_items[int(len(list_of_items) * 0.8):]

        for i in range(len(train_dict)):
            new_img_filename = str(i).zfill(6) + '.jpg'
            new_label_filename = str(i).zfill(6) + '.txt'
            dest_img = os.path.join(output_image_dir_train, new_img_filename)
            dest_label = os.path.join(output_label_dir_train, new_label_filename)
            copyfile(train_dict[i], dest_img)
            copyfile(matches[train_dict[i]], dest_label)
        for i in range(len(val_dict)):
            new_img_filename = str(i).zfill(6) + '.jpg'
            new_label_filename = str(i).zfill(6) + '.txt'
            dest_img = os.path.join(output_image_dir_val, new_img_filename)
            dest_label = os.path.join(output_label_dir_val, new_label_filename)
            copyfile(val_dict[i], dest_img)
            copyfile(matches[val_dict[i]], dest_label)

    else:
        output_image_dir = os.path.join(output_image_dir, 'test')
        output_label_dir = os.path.join(output_label_dir, 'test')

        for i in range(len(list_of_items)):
            new_img_filename = str(i).zfill(6) + '.jpg'
            new_label_filename = str(i).zfill(6) + '.txt'
            dest_img = os.path.join(output_image_dir, new_img_filename)
            dest_label = os.path.join(output_label_dir, new_label_filename)
            copyfile(list_of_items[i], dest_img)
            copyfile(matches[list_of_items[i]], dest_label)
        print(list_of_items[0])
        print(matches[list_of_items[0]])



if __name__ == '__main__':
    train_dir = '/mnt/disk1/Yudong/datasets/MOT20/train'
    test_dir = '/mnt/disk1/Yudong/datasets/MOT20/test'
    output_dir = '/mnt/disk1/Yudong/datasets/MOT20-det/'
    load_data(train_dir, True, output_dir)
    load_data(test_dir, False, output_dir)
    # test_dict = {1:1, 2:2, 3:3, 4:4}
    # test_list = [1,2,3,4]
    # t1 = test_list[int(len(test_list)/2):]
    # print(t1)
    # d1 = dict(list(test_dict.items())[int(len(test_dict)*0.8):])
    # print(d1)