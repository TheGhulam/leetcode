#Problem 624: Maximum Distance in Arrays

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        imin, imax = arrays[0][0], arrays[0][-1]
        res = 0

        for i in range(1, len(arrays)):
            curmin, curmax = arrays[i][0], arrays[i][-1]

            res = max(res,
            abs(imax-curmin),
            abs(curmax-imin))

            imax = max(imax, curmax)
            imin = min(imin, curmin)
        
        return res