#Problem 2924: Find Champion II

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = [0] * n

        for start, end in edges:
            incoming[end] += 1

        o = []
        for i, count in enumerate(incoming):
            if not count:
                o.append(i)
        
        if len(o) > 1: return -1
        return o[0]