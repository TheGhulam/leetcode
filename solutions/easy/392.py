#Problem 392: Is Subsequence
#Difficulty: Easy

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    print(Solution().isSubsequence(s, t)) # True
    s = "axc"
    t = "ahbgdc"
    print(Solution().isSubsequence(s, t)) # False
    s = "abc"
    t = ""
    print(Solution().isSubsequence(s, t)) # False
    s = ""
    t = "ahbgdc"
    print(Solution().isSubsequence(s, t)) # True