#Problem 139: Word Break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict) #O(1) Lookups

        # dp[i] represents whether the substring s[0:i] can be segmented into words from the dictionary
        dp = [False] * (len(s)+1)
        dp[0] = True

        for r in range(1, len(s)+1):
            for l in range(r):
                if dp[l] and s[l:r] in words:
                    dp[r] = True
                    break
        
        return dp[-1]