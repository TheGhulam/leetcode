#Problem 96: Unique Binary Search Trees

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = dp[0] = 1

        for nodes in range(2, n+1):
            for root in range(1, nodes+1):
                left_nodes = root - 1
                right_nodes = nodes - root
                dp[nodes] += dp[left_nodes] * dp[right_nodes]
        
        return dp[n]