class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        new = [intervals[0]]
        count = 0
        for start, end in intervals[1:]:
            if new[-1][1] > start:
                # keep the one with min end
                if end < new[-1][1]:
                    new[-1] = [start, end]
                count += 1
            else:
                new.append([start, end])
        print(new)
        return count
        
