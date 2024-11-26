#Problem 15: 3Sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []

        nums.sort()
        n = len(nums)
        o = []

        if nums[0] > 0 or nums[-1] < 0: return []

        # Convert to two sum
        for i in range(n-2):
            # Skip Duplicates
            if i > 0 and nums[i] == nums[i-1]: continue

            # Early termination
            if nums[i] + nums[i+1] + nums[i+2] > 0: break
            if nums[i+1] + nums[n-2] + nums[n-1] < 0: continue

            l = i + 1
            r = n - 1
            target = -nums[i]

            while l < r:
                s = nums[l] + nums[r]

                if s == target:
                    o.append([nums[i], nums[l], nums[r]])

                    # Skip duplicates
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]: l += 1
                    while l < r and nums[r] == nums[r+1]: r -= 1
                
                elif s < target:
                    l += 1
                else:
                    r -= 1

        return o