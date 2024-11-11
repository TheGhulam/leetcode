#Problem 53: Maximum Subarray

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = max_global = nums[0]

        # Kadane's Algo
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            if max_current >= max_global:
                max_global = max_current

        return max_global

if __name__ == "__main__":
    solution = Solution()

    # Expected: 6
    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

    # Expected: 1
    print(solution.maxSubArray([1]))

    # Expected: 23
    print(solution.maxSubArray([5,4,-1,7,8]))