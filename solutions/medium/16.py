#Problem 16: 3Sum Closest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        abs_s = float('inf')
        s = 0

        for i in range(n-2):
            l = i+1
            r = n-1

            while l < r:
                curr_s = nums[i]+nums[l]+nums[r]
                diff = curr_s - target
                if abs(diff) < abs_s:
                    abs_s = abs(diff)
                    s = curr_s

                if curr_s < target:
                    l += 1
                else:
                    r -= 1
        return s