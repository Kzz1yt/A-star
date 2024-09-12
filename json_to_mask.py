import os
import json
import numpy as np
import cv2

def json_to_mask(json_file, output_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    img_height = data['imageHeight']
    img_width = data['imageWidth']
    mask = np.zeros((img_height, img_width), dtype=np.uint8)

    for shape in data['shapes']:
        label = shape['label']
        points = shape['points']
        polygon_points = np.array(points, dtype=np.int32)
        cv2.fillPoly(mask, [polygon_points], 255)

    cv2.imwrite(output_file, mask)

# 示例用法
input_dir = '3'
output_dir = '4'

# 遍历目录中的所有JSON文件
for filename in os.listdir(input_dir):
    if filename.endswith('.json'):
        json_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, filename.replace('.json', '.png'))
        json_to_mask(json_file, output_file)