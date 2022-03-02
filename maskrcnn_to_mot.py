import pandas as pd
import numpy as np

labels_dir = '/mnt/disk1/Yudong/optimized_bb/2019_09_29_ONRD001_filtered_car_only_.txt'
df = pd.read_csv(labels_dir, sep=' ', header=None)
df_result = pd.DataFrame()
map = {'Car': 0}
classes = np.zeros(df.shape[0]).astype(int)
x_y_z = (np.zeros(df.shape[0])-1).astype(int)
df_result['frame_id'] = df[0]
df_result['class'] = classes
df_result['left'] = df[17]
df_result['top'] = df[18]
df_result['width'] = abs(df[17]-df[19])
df_result['height'] = abs(df[18]-df[20])
df_result['conf'] = df[24]
df_result['x'] = x_y_z
df_result['y'] = x_y_z
df_result['z'] = x_y_z
df_result.to_csv('/mnt/disk1/Yudong/optimized_bb/det.txt', sep=',', index=False, header=False)
print(df_result)