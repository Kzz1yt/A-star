from PIL import Image
import os

# 定义函数来批量转换图像格式
def convert_jpg_to_png(image_path):
    try:
        # 打开图像
        image = Image.open(image_path)
        
        # 获取原始图像的路径和名称
        image_dir, image_name = os.path.split(image_path)
        
        # 构建新的文件路径和名称，将原始名称的后缀改为png
        new_image_path = os.path.join(image_dir, os.path.splitext(image_name)[0] + '.png')
        
        # 将图像转换为png格式并保存，这里使用了PNG的无损压缩格式
        image.save(new_image_path, format='PNG', lossless=True)
        
        print(f"Converted {image_path} to {new_image_path}")
        
        # 关闭图像
        image.close()
        
        # 删除原始jpg图像
        os.remove(image_path)
        
        print(f"Removed original jpg image {image_path}")
        
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

# 指定包含jpg图像的文件夹路径
jpg_folder = "skeles/masks"

# 遍历文件夹中的所有jpg图像并转换为png格式
for root, dirs, files in os.walk(jpg_folder):
    for file in files:
        if file.lower().endswith('.jpg'):
            jpg_path = os.path.join(root, file)
            convert_jpg_to_png(jpg_path)
