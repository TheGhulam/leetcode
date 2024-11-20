#Problem 1051: Height Checker

from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        minv, maxv = min(heights), max(heights)
        r = maxv-minv+1

        count = [0] * r
        for h in heights:
            count[h-minv] += 1

        s = 0
        h = 0
        for i in range(r):
            while count[i] > 0:
                if heights[h] != i + minv:
                    s += 1
                h += 1
                count[i] -= 1

        return s