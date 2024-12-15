#Problem 738: Monotone Increasing Digits

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = list(str(n))

        # Find the first decreasing digit
        i = 1
        while i < len(s) and s[i-1] <= s[i]:
            i += 1
        
        # Decrease the previous digit 
        while i > 0 and i < len(s) and s[i-1] > s[i]:
            s[i-1] = str(int(s[i-1]) - 1)
            i -= 1

        # Set all digits after the first decreasing digit to 9
        for j in range(i + 1, len(s)):
            s[j] = '9'
    
        return int(''.join(s))