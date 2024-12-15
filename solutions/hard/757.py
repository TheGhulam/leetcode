#Problem 757: Set Intersection Size At Least Two

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])  # Sort by end point
        points = []
        
        for start, end in intervals:
            # Find points that lie within current interval
            count = sum(1 for p in points if start <= p <= end)
            
            # Add needed points at the end of interval
            if count == 0:
                # Need two points - add them at end-1 and end
                points.append(end-1)
                points.append(end)
            elif count == 1:
                # Need one more point - but we need to be careful about placement
                # If the existing point is at end, add one at end-1
                # Otherwise add at end
                if points[-1] == end:
                    points.append(end-1)
                else:
                    points.append(end)
        
        return len(points)