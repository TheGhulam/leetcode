#Problem 409: Longest Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for c in s: 
            count[c] = count.get(c, 0) + 1

        l = 0
        has_odd = False

        for c in count.values():
            l += (c//2)*2
            if c % 2 == 1:
                has_odd = True
        
        return l + 1 if has_odd else l