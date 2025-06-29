# Last updated: 6/29/2025, 8:11:31 AM
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        output = 0
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            output += max(abs(x2 - x1), abs(y2 - y1))
        return output