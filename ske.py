import os
from skimage import io
from skimage.morphology import medial_axis

def extract_skeleton(input_folder):
    # 遍历输入文件夹中的所有图像文件
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # 构建图像文件的完整路径
            file_path = os.path.join(input_folder, filename)
            # 读取图像
            image = io.imread(file_path, as_gray=True)
            # 提取细化骨架
            skeleton, distance = medial_axis(image, return_distance=True)
            skeleton = (skeleton * 255).astype('uint8')  # 转换为uint8格式的图像
            # 构建保存细化骨架的文件路径
            output_filename = os.path.splitext(filename)[0] + '_ske' + os.path.splitext(filename)[1]
            output_path = os.path.join(input_folder, output_filename)
            # 保存细化骨架图像
            io.imsave(output_path, skeleton)

# 指定输入图像文件夹路径
input_folder = "test/masks2"
# 调用函数提取细化骨架并保存
extract_skeleton(input_folder)
