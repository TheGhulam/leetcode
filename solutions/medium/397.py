#Problem 397: Integer Replacement

# Greedy solution with bit manipulation
class Solution:
    def integerReplacement(n: int) -> int:
        # Counter for number of operations
        operations = 0
        
        # Continue until we reach 1
        while n != 1:
            # If number is even, divide by 2
            if n % 2 == 0:
                n = n // 2
            # If number is odd, we need to decide between +1 or -1
            else:
                # Special case for 3 since going to 2 is better than going to 4
                if n == 3:
                    n = n - 1
                # For other odd numbers, look at the binary representation
                # If the last two bits are '11', add 1 to get more trailing zeros
                # If the last two bits are '01', subtract 1 to get more trailing zeros
                elif (n & 2) == 2:  # checks if second-to-last bit is 1
                    n = n + 1
                else:
                    n = n - 1
            operations += 1
            
        return operations


# DP solution with memoization
class Solution:
    def integerReplacement(self, n: int) -> int:
        cache = {}
    
        def helper(num):
            if num == 1:
                return 0
            if num in cache:
                return cache[num]
                
            if num % 2 == 0:
                result = 1 + helper(num // 2)
            else:
                result = 1 + min(helper(num + 1), helper(num - 1))
                
            cache[num] = result
            return result
        
        return helper(n)