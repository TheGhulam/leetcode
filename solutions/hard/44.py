class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] represents if s[:i] matches p[:j]
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty pattern matches empty string
        dp[0][0] = True
        
        # Handle patterns starting with *
        # For example: "*abc" matching "abc"
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' can match current character or be empty
                    # dp[i][j-1]: treat '*' as empty
                    # dp[i-1][j]: use '*' to match current character
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    # Characters match or we have a '?'
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[m][n]