import pandas as pd
import os
import json
import numpy as np

def process_annotation(detection_dir, sequence_name, groundtruth, output_dir):
    sequences = []
    for sequence in sequence_name:
        sequence_dir = os.path.join(detection_dir, sequence)
        sequences.append(sequence_dir)

    print(sequences)

    outputs = []

    for sequence in sequences:
        print(sequence)
        sequence_table = pd.read_csv(sequence)
        sequence_table.region_attributes = sequence_table.region_attributes.apply(lambda x: json.loads(x))
        sequence_table.region_shape_attributes = sequence_table.region_shape_attributes.apply(lambda x: json.loads(x))
        sequence_table.filename = sequence_table.filename.apply(lambda x: int(x.replace(".jpg", "")))
        sequence_table["check"] = sequence_table.region_attributes.apply(lambda x: "tracking_id" in x.keys())
        check_table = sequence_table.loc[sequence_table["check"]==False]
        print(check_table)
        # classes = sequence_table.region_attributes.apply(lambda x: x["class"])
        if groundtruth:
            tracking_id = sequence_table.region_attributes.apply(lambda x: x["tracking_id"])
            tracking_id = tracking_id.apply(lambda x: x.replace("\n", ""))
        xs = sequence_table.region_shape_attributes.apply(lambda x: x["x"])
        ys = sequence_table.region_shape_attributes.apply(lambda x: x["y"])
        widths = sequence_table.region_shape_attributes.apply(lambda x: x["width"])
        heights = sequence_table.region_shape_attributes.apply(lambda x: x["height"])
        fodder = np.zeros(len(widths)) - 1
        fodder2 = np.zeros(len(widths)) + 1
        output = pd.DataFrame(
            columns=["index", "tracking_id", "x", "y", "width", "height", "confidence", "x1", "y1", "z1"])
        output["index"] = sequence_table.filename
        if groundtruth:
            output["tracking_id"] = tracking_id
        else:
            output["tracking_id"] = fodder
        output["x"] = xs
        output["y"] = ys
        output["width"] = widths
        output["height"] = heights
        if groundtruth:
            output["confidence"] = fodder2
        else:
            output["confidence"] = sequence_table.region_attributes.apply(lambda x: x["conf"])
        output["x1"] = fodder
        output["y1"] = fodder
        output["z1"] = fodder
        outputs.append(output)

        # print(sequence_table.region_attributes[0]["class"])
        # with open('test.txt', 'a') as f:
        #     outputAsString = outputs[0].to_string(header=False, index=False)
        #     f.write(outputAsString)

    for i in range(len(outputs)):
        output_dir1 = os.path.join(output_dir, sequence_name[i].replace("csv", "txt"))
        outputs[i].to_csv(output_dir1, header=False, index=False)

if __name__ == '__main__':
    detection_dir = "../../motmetrics/ground_truth"
    sequence_name = ["2019_05_28_CM1S013.csv", "2019_05_28_MLMS005.csv", "2019_05_28_PBMS006.csv", "2019_09_18_ONRD009.csv", "2019_09_29_ONRD012.csv"]
    output_dir = "../../motmetrics/ground_truth/clean"
    process_annotation(detection_dir, sequence_name, True, output_dir)
    # a = np.loadtxt('E:\\DevProjects\\CRUW\\test\\2019_09_18_ONRD009\\det\\det.txt', delimiter=',')