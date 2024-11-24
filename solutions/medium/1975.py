#Problem 1975: Maximum Matrix Sum

from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_abs = float('inf')
        s = 0
        odd_negative = False

        for r in matrix:
            for n in r:
                if n < 0:
                    odd_negative = not odd_negative
                s += abs(n)
                min_abs = min(min_abs, abs(n))
        
        if odd_negative:
            return s - 2*min_abs
        else:
            return s