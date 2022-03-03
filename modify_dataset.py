import os
import shutil

def modifiy_label_file(txt, dataset_dir, input_dir):
    sequence = txt.replace('.txt', '')
    dst = os.path.join(dataset_dir, sequence, 'det', 'det.txt')
    src = os.path.join(input_dir, txt)
    shutil.move(src, dst)

if __name__ == '__main__':
    input_base = '/mnt/disk1/Yudong/datasets/cruw_test_mot'
    dataset_dir = '/mnt/disk1/Yudong/datasets/cruw/test'
    txts = os.listdir(input_base)
    for txt in txts:
        modifiy_label_file(txt, dataset_dir,input_base)