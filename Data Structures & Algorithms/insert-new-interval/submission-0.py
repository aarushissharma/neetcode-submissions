class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals)
        new = [intervals[0]]

        for start, end in intervals[1:]: 
            if  start <= new[-1][1]:
                new[-1][1] = max(end, new[-1][1])
            else:
                new.append([start, end])
        return new
        