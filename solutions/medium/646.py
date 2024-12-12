#Problem 646: Maximum Length of Pair Chain

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        print(pairs)

        cur_end = -float('inf')
        res = 0

        for l, r in pairs:
            if l > cur_end:
                cur_end = r
                res += 1
        
        return res