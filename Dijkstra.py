import sys

# 定义结构体Dis用于记录最短路径信息
class Dis:
    def __init__(self):
        self.path = ""   # 记录路径
        self.value = 0   # 记录最短距离
        self.visit = False   # 标记是否已访问

# 定义有向图类Graph_DG
class Graph_DG:
    # 构造函数
    def __init__(self, vexnum, edge):
        self.vexnum = vexnum   # 顶点数
        self.edge = edge   # 边数
        # 初始化邻接矩阵为无穷大
        self.arc = [[float('inf')] * vexnum for _ in range(vexnum)]
        # 初始化最短路径信息数组
        self.dis = [Dis() for _ in range(vexnum)]

    # 判断输入的边的信息是否合法
    def check_edge_value(self, start, end, weight):
        if start < 1 or end < 1 or start > self.vexnum or end > self.vexnum or weight < 0:
            return False
        return True

    # 创建图
    def createGraph(self):
        print("Please enter the start and end points of each edge (vertex numbers start from 1), and its cost. Separate by Spaces and press Enter to enter the next one:")
        count = 0
        while count != self.edge:
            start, end, weight = map(int, input().split())
            while not self.check_edge_value(start, end, weight):
                print("This is illegal! please enter again.")
                start, end, weight = map(int, input().split())
            self.arc[start - 1][end - 1] = weight
            count += 1

    # 打印邻接矩阵
    def print_matrix(self):
        print("\nThe adjacency matrix of the graph is:")
        for row in self.arc:
            for weight in row:
                if weight == float('inf'):
                    print("∞", end=" ")
                else:
                    print(weight, end=" ")
            print()

    # Dijkstra算法
    def Dijkstra(self, begin):  
        for i in range(self.vexnum):
            self.dis[i].path = f"v{begin}-->v{i + 1}"
            self.dis[i].value = self.arc[begin - 1][i]
        self.dis[begin - 1].value = 0
        self.dis[begin - 1].visit = True

        count = 1
        while count != self.vexnum:
            temp = 0
            min_val = float('inf')
            for i in range(self.vexnum):
                if not self.dis[i].visit and self.dis[i].value < min_val:
                    min_val = self.dis[i].value
                    temp = i

            self.dis[temp].visit = True
            count += 1

            for i in range(self.vexnum):
                if not self.dis[i].visit and self.arc[temp][i] != float('inf') and (self.dis[temp].value + self.arc[temp][i]) < self.dis[i].value:
                    self.dis[i].value = self.dis[temp].value + self.arc[temp][i]
                    self.dis[i].path = f"{self.dis[temp].path}-->v{i + 1}"

    # 打印最短路径
    def print_path(self, begin):
        print(f"\nThe shortest path of the graph starting from v{begin} is:")
        for i in range(self.vexnum):
            if self.dis[i].value != float('inf'):
                print(f"{self.dis[i].path}={self.dis[i].value}")
            else:
                print(f"{self.dis[i].path} has no shortest path")

# 检查输入的顶点数和边数是否合法
def check(Vexnum, edge):
    if Vexnum <= 0 or edge <= 0 or (Vexnum * (Vexnum - 1)) // 2 < edge:
        return False
    return True


def main():
    # 输入图的顶点个数和边的条数
    vexnum, edge = map(int, input("Enter the number of vertices and edges of the graph, use the Space bar to separate and press Enter to end: \n").split())
    while not check(vexnum, edge):
        print("This is illegal! please enter again.")
        vexnum, edge = map(int, input().split())

    # 创建图对象
    graph = Graph_DG(vexnum, edge)
    # 创建图
    graph.createGraph()
    # 打印邻接矩阵
    graph.print_matrix()
    # 进行Dijkstra算法求解最短路径，并打印最短路径
    graph.Dijkstra(1)
    graph.print_path(1)

if __name__ == "__main__":
    main()
