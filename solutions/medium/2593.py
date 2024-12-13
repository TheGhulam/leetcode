#Problem 2593: Find Score of an Array After Marking All Elements

import numpy as np
from typing import List

# Does not work on leetcode because of numpy
# without NumPy, Python's sorted() with enumerate() might handle ties differently
class Solution:
    def findScore(self, nums: List[int]) -> int:
        inp = np.array(nums)
        sorted_indices = np.argsort(inp)
        boolean_indices = [False] * len(nums)
        sorted_nums = inp[sorted_indices]
        zipped = zip(sorted_nums, sorted_indices)

        res = 0
        for n, i in zipped:
            if boolean_indices[i]:
                continue
            res += n
            boolean_indices[i] = True
            if i + 1 < len(nums):
                boolean_indices[i+1] = True
            if i - 1 >= 0:
                boolean_indices[i-1] = True
        
        return int(res)

class Solution:
    def findScore(self, nums: List[int]) -> int:
        # Create (value, index) pairs and sort by value
        # Use index as secondary sort key to maintain stable ordering
        pairs = [(num, i) for i, num in enumerate(nums)]
        pairs.sort(key=lambda x: (x[0], x[1]))  # Sort by value first, then by index
        
        marked = [False] * len(nums)
        score = 0
        
        for num, idx in pairs:
            if not marked[idx]:
                score += num
                marked[idx] = True
                if idx + 1 < len(nums):
                    marked[idx + 1] = True
                if idx - 1 >= 0:
                    marked[idx - 1] = True
        
        return score
