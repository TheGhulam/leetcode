#Problem 5: Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return 0
        n = len(s)

        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        l = r = 0

        for i in range(n):
            #Odd length
            l1, r1 = expand(i, i)
            if r1-l1 > r-l:
                l, r = l1, r1
            
            #Even length
            l1, r1 = expand(i, i+1)
            if r1-l1 > r-l:
                l, r = l1, r1
        
        return s[l:r+1]