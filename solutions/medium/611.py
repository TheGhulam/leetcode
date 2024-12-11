#Problem 611: Valid Triangle Number

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        res = 0
        for i in range(n-1, 1, -1):
            l, r = 0, i-1

            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    res += r - l
                    r -= 1
                else:
                    l += 1 # Sum too small, need larger
    
        return res