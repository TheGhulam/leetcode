#Problem 2461: Maximum Sum of Distinct Subarrays With Length K

from typing import List 

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


if __name__ == "__main__":
    s = Solution()
    print(s.maximumSubarraySum([1,2,1,2,6,7,5,1], 2))  # 13
    print(s.maximumSubarraySum([1,2,1,2,6,7,5,1], 3))  # 18
    print(s.maximumSubarraySum([1,2,1,2,6,7,5,1], 4))  # 21
    print(s.maximumSubarraySum([1,2,1,2,6,7,5,1], 5))  # 22
    print(s.maximumSubarraySum([1,2,1,2,6,7,5,1], 6))  # 0
    print(s.maximumSubarraySum([1,2,1,2,6,7,5,1], 7))  # 0
    print(s.maximumSubarraySum([1,2,3,4,6,7,5,1], 7))  # 28