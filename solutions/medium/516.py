#Problem 516: Longest Palindromic Subsequence

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n) for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for len_substr in range(2, n+1):
            for i in range(n-len_substr+1):
                j = i + len_substr - 1

                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][n-1]