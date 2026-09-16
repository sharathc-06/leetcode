import random
import math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        angle = random.uniform(0, 2 * math.pi)
        r = self.r * math.sqrt(random.random())

        x = self.x + r * math.cos(angle)
        y = self.y + r * math.sin(angle)

        return [x, y]