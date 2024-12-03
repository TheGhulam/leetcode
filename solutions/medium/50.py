#Problem 50:Powx n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
            
        # Handle negative power
        if n < 0:
            x = 1/x
            n = -n
            
        result = 1
        current_product = x
        
        # Binary exponentiation
        while n > 0:
            # If current bit is 1, multiply result by current_product
            if n & 1:
                result *= current_product
            # Square the current_product for next bit
            current_product *= current_product
            # Right shift n by 1
            n >>= 1
            
        return result