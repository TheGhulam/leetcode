#Problem 402: Remove K Digits

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num): return "0"

        stack = []

        for d in num:
            while k > 0 and stack and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)
        
        # If we still have digits to remove, remove from the end
        # This handles cases like "123456" where digits are in ascending order
        while k > 0:
            stack.pop()
            k -= 1
        
        result = ''.join(stack)
        result = result.lstrip('0')
        return result if result else "0"