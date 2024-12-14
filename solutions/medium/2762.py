#Problem 2762: Continuous Subarrays

from collections import deque

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        s = 0
        max_dq = deque()  # monotonic decreasing queue for maximum
        min_dq = deque()  # monotonic increasing queue for minimum

        for e in range(n):
            while max_dq and nums[max_dq[-1]] < nums[e]:
                max_dq.pop()
            max_dq.append(e)
            
            while min_dq and nums[min_dq[-1]] > nums[e]:
                min_dq.pop()
            min_dq.append(e)

            # Shrink window while it's not continuous
            while max_dq and min_dq and nums[max_dq[0]] - nums[min_dq[0]] > 2:
                s += 1
                while max_dq and max_dq[0] < s:
                    max_dq.popleft()
                while min_dq and min_dq[0] < s:
                    min_dq.popleft()

            res += e - s + 1
        
        return res