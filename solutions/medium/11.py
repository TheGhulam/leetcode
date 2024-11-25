#Problem 11: Container With Most Water

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        a = 0

        while l < r:
            w = r - l
            h = min(height[l], height[r])
            a = max(a, w*h)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return a