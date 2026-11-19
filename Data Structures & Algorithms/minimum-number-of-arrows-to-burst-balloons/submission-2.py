class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        arrow = [points[0]]
        for start, end in points[1:]:
            if arrow[-1][1] >= start:
                arrow[-1][1] = min(arrow[-1][1], end)
            else:
                arrow.append([start, end])
        return len(arrow)
        

