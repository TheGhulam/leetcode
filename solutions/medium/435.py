#Problem 435: Non-overlapping Intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        prev_end = intervals[0][1]

        res = 0
        for s, e in intervals[1:]:
            if s < prev_end:
                res += 1
            else:
                prev_end = e
        
        return res