#Problem 330: Patching Array

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = covered = i = 0

        while covered < n:
            if i < len(nums) and nums[i] <= covered + 1:
                covered += nums[i]
                i += 1
            else:
                patches += 1
                covered += (covered + 1)
        
        return patches