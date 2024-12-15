#Problem 680: Valid Palindrome II

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            return s == s[::-1]

        l, r = 0, len(s)-1

        while l < r:
            if s[l] != s[r]:
                return isPalindrome(s[l+1:r+1]) or isPalindrome(s[l:r])
            l += 1
            r -= 1

        return True 