#Problem 32: Longest Valid Parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s or len(s) < 2: return 0

        res = 0
        stack = [-1]

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i-stack[-1])

        
        return res