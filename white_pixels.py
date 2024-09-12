import cv2

def count_white_pixels(image_path):
    # 读取图像
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # 计算白色像素点个数
    num_white_pixels = cv2.countNonZero(image)
    return num_white_pixels

# 示例用法
image_path = "test\\masks2\\455-2.png"  # 替换为实际图像文件路径
white_pixel_count = count_white_pixels(image_path)
print("Number of white pixels:", white_pixel_count)
