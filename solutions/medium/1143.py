#Problem 1143: Longest Common Subsequence

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        grid = [[0] * (m+1) for _ in range(n+1)]

        for r in range(1, n+1):
            for c in range(1, m+1):
                if text1[r-1] == text2[c-1]:
                    grid[r][c] = 1 + grid[r-1][c-1]
                else:
                    grid[r][c] = max(grid[r-1][c], grid[r][c-1])
        

        return grid[n][m]

        # If we want to return the subsequence:
        # subsequence = ""
        # r, c = n, m
        # while r > 0 and c > 0:
        #     if text1[r-1] == text2[c-1]:
        #         subsequence = text1[r-1] + subsequence
        #         r -= 1
        #         c -= 1
        #     elif grid[r-1][c] > grid[r][c-1]:
        #         r -= 1
        #     else:
        #         c -= 1