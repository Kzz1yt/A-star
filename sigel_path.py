import cv2
import numpy as np
import time

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent  # 父节点
        self.position = position  # 当前节点的位置坐标

        self.g = 0  # 起始点到当前节点的实际代价
        self.h = 0  # 当前节点到目标节点的估算代价（启发式函数）
        self.f = 0  # f = g + h，综合代价

    def __eq__(self, other):
        return self.position == other.position

def astar_search(start, end, grid):
    open_list = []  # 存放待访问的节点
    closed_list = []  # 存放已访问的节点

    open_list.append(start)  # 将起始节点加入待访问列表

    while open_list:
        current_node = open_list[0]  # 从待访问列表中选取f值最小的节点作为当前节点
        current_index = 0

        # 找到f值最小的节点
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # 将当前节点从待访问列表移除，并加入已访问列表
        open_list.pop(current_index)
        closed_list.append(current_node)

        # 判断是否到达目标节点
        if current_node == end:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        # 生成当前节点的邻居节点
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # 确保节点在地图范围内
            if node_position[0] > (len(grid) - 1) or node_position[0] < 0 or node_position[1] > (len(grid[len(grid)-1]) -1) or node_position[1] < 0:
                continue

            # 检查节点是否是障碍物
            if grid[node_position[0]][node_position[1]] != 255:
                continue

            new_node = Node(current_node, node_position)

            children.append(new_node)

        # 处理每一个邻居节点
        for child in children:
            # 如果邻居节点已经在已访问列表中，则跳过
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # 计算邻居节点的代价
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end.position[0]) ** 2) + ((child.position[1] - end.position[1]) ** 2)
            child.f = child.g + child.h

            # 如果邻居节点已经在待访问列表中，并且新路径代价更高，则跳过
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # 将邻居节点加入待访问列表
            open_list.append(child)

def mouse_callback(event, x, y, flags, param):
    global start, end, image, path, shortest_length
    if event == cv2.EVENT_LBUTTONDOWN:
        if start is None:
            start = (y, x)
            print("Start point:", start)
        elif end is None:
            end = (y, x)
            print("End point:", end)
            start_node = Node(None, start)
            end_node = Node(None, end)
            path = astar_search(start_node, end_node, image)
            shortest_length = len(path)
            print("Shortest path length:", shortest_length, "pixels")
            for position in path:
                image[position[0]][position[1]] = 100

            # 画出路径，颜色为绿色
            for point in path:
                cv2.circle(image, (point[1], point[0]), 1, (0, 255, 0), -1)

            cv2.imshow('Pathfinding', image)
            # print("Time taken:", time.time() - start_time, "s")

            # 计算图像尺寸
            length = image.shape[0]
            width = image.shape[1]
            # image_size = image.shape[0] * image.shape[1]
            print("image_size =", length,"*",width, "pixels")
            image_size = length * width

            # 计算实际长度
            input_size = 810 * 224  # mm
            # 计算比例尺
            scale = input_size / image_size
            # 计算实际长度
            actual_length = shortest_length * scale
            print("Actual length = ", actual_length, "mm")

            cv2.waitKey(0)
            cv2.destroyAllWindows()

def main():
    global start, end, image, path, shortest_length, start_time
    # 读取图像
    image = cv2.imread('4\\1_mirror.png', 0)
 
    start = None
    end = None
    path = []
    shortest_length = 0

    cv2.namedWindow('Pathfinding')
    cv2.setMouseCallback('Pathfinding', mouse_callback)

    while True:
        cv2.imshow('Pathfinding', image)
        key = cv2.waitKey(1)
        if key == 27:  # ESC
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    start_time = time.time()
    main()
