#Problem 452: Minimum Number of Arrows to Burst Balloons

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        res = 1
        current_arrow = points[0][1]

        for s, e in points[1:]:
            if s > current_arrow:
                res +=1 
                current_arrow = e
        
        return res