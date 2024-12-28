#Problem 689: Maximum Sum of 3 Non-Overlapping Subarrays

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        # Function to get sum of subarray starting at index i with length k
        def get_subarray_sum(i):
            return prefix_sum[i + k] - prefix_sum[i]
        
        # dp[i][j] represents the maximum sum possible using j + 1 subarrays 
        # considering the array up to index i
        dp = [[0] * 3 for _ in range(n)]
        
        # pos[i][j] stores the starting position of the last subarray used
        # in the optimal solution for dp[i][j]
        pos = [[0] * 3 for _ in range(n)]
        
        # Initialize first window sum
        dp[k-1][0] = get_subarray_sum(0)
        
        # Fill dp table for first array (j=0)
        for i in range(k, n):
            curr_sum = get_subarray_sum(i-k+1)
            if curr_sum > dp[i-1][0]:
                dp[i][0] = curr_sum
                pos[i][0] = i-k+1
            else:
                dp[i][0] = dp[i-1][0]
                pos[i][0] = pos[i-1][0]
        
        # Fill dp table for second and third arrays
        for j in range(1, 3):
            for i in range((j+1)*k-1, n):
                # Don't take current window
                dp[i][j] = dp[i-1][j]
                pos[i][j] = pos[i-1][j]
                
                # Take current window
                curr_sum = get_subarray_sum(i-k+1)
                prev_sum = dp[i-k][j-1]
                
                if curr_sum + prev_sum > dp[i][j]:
                    dp[i][j] = curr_sum + prev_sum
                    pos[i][j] = i-k+1
        
        # Backtrack to find positions
        result = []
        curr = n-1
        for j in range(2, -1, -1):
            result.insert(0, pos[curr][j])
            curr = pos[curr][j] - 1
            
        return result