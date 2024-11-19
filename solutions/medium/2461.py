#Problem 2461: Maximum Sum of Distinct Subarrays With Length K

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        o = 0
        count = defaultdict(int)
        s = 0

        l = 0
        for r in range(0, len(nums)):
            s += nums[r]
            count[nums[r]] += 1

            if r-l+1 > k:
                s -= nums[l]
                count[nums[l]] -= 1
                if count[nums[l]] == 0: count.pop(nums[l])
                l += 1

            if len(count) == r - l + 1 == k:
                o = max(o, s)
        
        return o