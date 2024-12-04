#Problem 316: Remove Duplicate Letters

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {c: i for i, c in enumerate(s)}
        used = set()
        stack = []

        for i, c in enumerate(s):
            if c not in used:
                # Remove chars that are larger than current char and will appear later in string
                while stack and c < stack[-1] and i < last_occ[stack[-1]]:
                    used.remove(stack.pop())

                stack.append(c)
                used.add(c)
        
        return ''.join(stack)