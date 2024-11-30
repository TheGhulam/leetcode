#Problem 91: Decode Ways

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': return 0
        n = len(s)

        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            one_digit = int(s[i-1])
            two_digits = int(s[i-2:i])

            # If current digit is valid (1-9)
            if one_digit > 0:
                dp[i] += dp[i-1]
                
            # If previous two digits form valid number (10-26)
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]