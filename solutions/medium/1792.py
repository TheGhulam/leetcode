#Problem 1792: Maximum Average Pass Ratio

from heapq import heappush, heappop

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def improvement(pass_count, total):
            return (pass_count + 1)/(total+1) - (pass_count/total)

        # (improvement, pass_count, total)
        heap = [] 

        for p, t in classes:
            imp = improvement(p, t)
            heappush(heap, (-imp, p, t))
        
        for _ in range(extraStudents):
            i, p, t = heappop(heap)
            imp = improvement(p+1, t+1)
            heappush(heap, (-imp, p+1, t+1))
        
        res = 0
        for _, p, t in heap:
            res += p/t
        
        return res/len(classes)