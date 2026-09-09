from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0

        for i in range(len(points)):

            distances = defaultdict(int)

            for j in range(len(points)):
                if i == j:
                    continue

                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]

                distance = dx * dx + dy * dy

                distances[distance] += 1

            for count in distances.values():
                result += count * (count - 1)

        return result