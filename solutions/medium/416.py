#Problem 416: Partition Equal Subset Sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        if s % 2 != 0: return False

        t = s // 2

        dp = [False] * (t+1)
        dp[0] = True

        for n in nums:
            # We iterate from t to n-1 because we don't want to consider the same element twice
            for j in range(t, n-1, -1):
                # If we can make the sum j-n, we can make the sum j
                dp[j] = dp[j] or dp[j-n]

        return dp[t]