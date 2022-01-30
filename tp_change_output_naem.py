import os

dir = '/mnt/disk1/Yudong/2019_09_29_ONRD004'
list_image = os.listdir(dir)
for image in list_image:
    old_image_dir = os.path.join(dir, image)
    new_image_name = image.replace('.png', '').zfill(6) + '.png'
    new_image_dir = os.path.join(dir, new_image_name)
    os.rename(old_image_dir, new_image_dir)