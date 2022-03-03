import os

def generate_command(sequence_name):
    command = f'python deep_sort_app.py --sequence_dir=/mnt/disk1/Yudong/datasets/cruw/test/{sequence_name} --detection_file=/mnt/disk1/Yudong/deep_sort/resources/detections/cruw/{sequence_name}.npy --min_confidence=0.3 --nn_budget=100 --output_file=resources/output/{sequence_name}.txt --display_output=/mnt/disk1/Yudong/datasets/cruw/test_vis/{sequence_name}'
    return command

if __name__ == '__main__':
    input_dir = '/mnt/disk1/Yudong/datasets/cruw/test'
    sequences = os.listdir(input_dir)
    result = []
    for sequence in sequences:
        command = generate_command(sequence)
        print(command)
