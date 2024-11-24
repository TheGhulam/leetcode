#Problem 45: Jump Game II

from typing import List

# Dynamic Programming
# Time: O(n^2)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [float('inf')] * (n)
        dp[0] = 0

        for i in range(n):
            for j in range(1, nums[i]+1):
                if i + j >= n: break
                dp[i+j] = min(dp[i+j], (1+dp[i]))
        
        return dp[n-1]

# Greedy
# Time: O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return 0
            
        jumps = 0 
        current_max_reach = 0
        next_max_reach = 0
        
        for i in range(n - 1):
            next_max_reach = max(next_max_reach, i + nums[i])
            
            # If we've reached the current_max_reach, we must jump
            if i == current_max_reach:
                jumps += 1
                current_max_reach = next_max_reach
                
                # If we can already reach the end, no need to keep checking
                if current_max_reach >= n - 1:
                    break
        
        return jumps