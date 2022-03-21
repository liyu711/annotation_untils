import os
import shutil

if __name__ == '__main__':
    base_dir = '../ROD2121_cfar/'
    cfar_dir = os.path.join(base_dir, 'cfar_dets')
    files = os.listdir(os.path.join(base_dir, 'cfar_dets'))
    test_dir = '../ROD2021/annotations/test'
    test_files = os.listdir(test_dir)
    temp = (map(lambda x: x.lower(), test_files))
    test_clean = list(temp)
    target_test_dir = os.path.join(base_dir, 'test')
    target_train_dir = os.path.join(base_dir, 'train')
    for file in files:
        move_from = os.path.join(cfar_dir, file)
        if file in test_clean:
            move_to = os.path.join(target_test_dir, file)
            shutil.move(move_from, move_to)
        else:
            move_to = os.path.join(target_train_dir, file)
            shutil.move(move_from, move_to)



