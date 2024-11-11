#Problem 383: Ransom Note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mchars = {}
        for c in magazine:
            mchars[c] = 1 + mchars.get(c, 0)
        
        for c in ransomNote:
            if c in mchars and mchars[c] > 0:
                mchars[c] -= 1
            else: return False
        return True