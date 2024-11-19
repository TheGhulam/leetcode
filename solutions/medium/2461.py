#Problem 2461: Maximum Sum of Distinct Subarrays With Length K

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        o = 0
        last_i = {}
        s = 0

        l = 0
        for r in range(0, len(nums)):
            s += nums[r]
            i = last_i.get(nums[r], -1)
            last_i[nums[r]] = r
            
            while l <= i or r-l+1 > k:
                s -= nums[l]
                l += 1

            if r - l + 1 == k:
                o = max(o, s)
        
        return o