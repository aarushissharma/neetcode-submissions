class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        new = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= new[-1][1]:
                new[-1][1] = max(new[-1][1], end)
            else:
                new.append([start, end])
        return new