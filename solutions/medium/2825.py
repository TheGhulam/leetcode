#Problem 2825: Make String a Subsequence Using Cyclic Increments

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = 0

        for i in range(len(str1)):
            if j < len(str2):
                if str1[i] == str2[j] or chr((ord(str1[i])-97+1)%26+97) == str2[j]:
                    j += 1
        
        return j == len(str2)