#Problem 561: Array Partition

from typing import List

# O(nlogn) solution
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])

    
# O(n+k) solution
# k = range of numbers in nums
# Performance is better when k is small
# But for large k, this solution is slower than the O(nlogn) solution

class Solution1:
    def arrayPairSum(self, nums: List[int]) -> int:
        minv, maxv = min(nums), max(nums)
        r = maxv - minv + 1

        count = [0] * r
        for n in nums:
            count[n - minv] += 1

        s = 0
        need_pair = False
        for i in range(r):
            while count[i] > 0:
                if not need_pair:
                    s += i + minv
                need_pair = not need_pair
                count[i] -= 1
        
        return s

if __name__ == "__main__":
    print(Solution().arrayPairSum([1,4,3,2]))  # 4
    print(Solution().arrayPairSum([6,2,6,5,1,2]))  # 9
    print(Solution().arrayPairSum([1,2,3,2]))  # 3
    print(Solution().arrayPairSum([1,2,3,4]))  # 4
    print(Solution().arrayPairSum([1,2,3,4,5,6]))  # 9
    print(Solution().arrayPairSum([1,2,3,4,5,6,7,8]))  # 16