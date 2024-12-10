#Problem 581: Shortest Unsorted Continuous Subarray

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return 0

        l = 0
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                l = i - 1
                break
        else:
            return 0
        
        r = n-1
        for i in range(n-2, -1, -1):
            if nums[i] > nums[i+1]:
                r = i + 1
                break
        
        min_val, max_val = min(nums[l:r+1]), max(nums[l:r+1])

        for i in range(l):
            if nums[i] > min_val:
                l = i
                break

        for i in range(n-1, r, -1):
            if nums[i] < max_val:
                r = i
                break

        return r - l + 1