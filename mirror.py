import os
import cv2

def mirror_images(input_folder, output_folder):
    # 创建输出文件夹（如果不存在）
    os.makedirs(output_folder, exist_ok=True)
    
    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        # 构建输入文件的完整路径
        input_path = os.path.join(input_folder, filename)
        
        # 检查文件是否是图像文件
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            # 读取图像
            image = cv2.imread(input_path)
            
            # 检查是否成功读取图像
            if image is None:
                print(f"Failed to read image: {input_path}")
                continue
            
            # 创建镜像样本（水平翻转）
            mirrored_image = cv2.flip(image, 1)  # 1 表示水平翻转
            
            # 构建输出文件的完整路径
            output_filename = os.path.splitext(filename)[0] + "_mirror" + os.path.splitext(filename)[1]
            output_path = os.path.join(output_folder, output_filename)
            
            # 保存镜像样本到输出文件夹
            cv2.imwrite(output_path, mirrored_image)
            
            print(f"Saved mirrored image: {output_path}")

# 示例用法
input_folder = '1'  # 输入文件夹路径
output_folder = '3'  # 输出文件夹路径

mirror_images(input_folder, output_folder)
