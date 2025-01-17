# random_map.py

import numpy as np
import point
from matplotlib.patches import Rectangle

class RandomMap:
    def __init__(self, size=50):    # Default map size
        self.size = size
        self.obstacle = size//8     # Random obstacles account for 1/8 of the total area
        self.GenerateObstacle()

    def GenerateObstacle(self):     # Generate obstacles
        self.obstacle_point = []
        self.obstacle_point.append(point.Point(self.size//2, self.size//2))
        self.obstacle_point.append(point.Point(self.size//2, self.size//2-1))


        # Generate an obstacle in the middle
        for i in range(self.size//2-4, self.size//2):
            self.obstacle_point.append(point.Point(i, self.size-i))
            self.obstacle_point.append(point.Point(i, self.size-i-1))
            self.obstacle_point.append(point.Point(self.size-i, i))
            self.obstacle_point.append(point.Point(self.size-i, i-1))

        for i in range(self.obstacle-1):    # Map area constraints
            x = np.random.randint(0, self.size)
            y = np.random.randint(0, self.size)
            self.obstacle_point.append(point.Point(x, y))

            if (np.random.rand() > 0.5): # Random boolea---True: vertical direction, False: horizontal direction
                for l in range(self.size//4):   # The extension length is 1/4 of the map
                    self.obstacle_point.append(point.Point(x, y+l))
                    pass
            else:
                for l in range(self.size//4):
                    self.obstacle_point.append(point.Point(x+l, y))
                    pass

        
    def IsObstacle(self, i ,j):      # Checks if the given coordinates are an obstacle
        for p in self.obstacle_point:
            if i==p.x and j==p.y:
                return True
        return False
    
    # def draw_map(self, ax):
    #     for p in self.obstacle_point:
    #         rec = Rectangle((p.x, p.y), 4, 5, color='black')
    #         ax.add_patch(rec)