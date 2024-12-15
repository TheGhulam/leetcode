#Problem 678: Valid Parenthesis String

class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = max_open = 0

        for c in s:
            if c == "(":
                min_open += 1
                max_open += 1
            elif c == ")":
                min_open -= 1
                max_open -= 1
            else:
                min_open -= 1
                max_open += 1
            
            if max_open < 0: return False
            min_open = max(0, min_open)

        return min_open == 0