import os
import pandas as pd
import numpy as np

def filter_by_size(dir, area):
    df = pd.read_csv(dir,sep=',',header=None)
    df_result = df[df[4] * df[5] > area]
    return df_result

if __name__ == '__main__':
    input_dir = '/mnt/disk1/Yudong/datasets/cruw_test_mot'
    output_dir = '/mnt/disk1/Yudong/datasets/cruw_test_mot_filtered_size'
    txts = os.listdir(input_dir)
    for txt in txts:
        input_path = os.path.join(input_dir, txt)
        output_path = os.path.join(output_dir, txt)
        result_df = filter_by_size(input_path, 900)
        result_df.to_csv(output_path, sep=',',index=False, header=False)