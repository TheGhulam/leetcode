from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l + r)//2
            if target == nums[m]:
                return m
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]

    solution = Solution()

    test_targets = [0, 3]  # testing with target 0 (exists) and 3 (doesn't exist)

    for target in test_targets:
        result = solution.search(nums, target)
        print(f"Search for {target} in {nums}")
        print(f"Result: {result}")
        print()
