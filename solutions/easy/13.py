#Problem 13: Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        o = 0
        i = 0
        while i < len(s):
            if s[i] == "I":
                if i + 1 < len(s):
                    if s[i+1] == "V":
                        o += 4
                        i += 2
                    elif s[i+1] == "X":
                        o += 9
                        i += 2
                    elif i + 2 < len(s) and s[i+1] == "I" and s[i+2] == "I":
                        o += 3
                        i += 3
                    elif s[i+1] == "I":
                        o += 2
                        i += 2
                    else:
                        o += 1
                        i += 1
                else:
                    o += 1
                    i += 1
            elif s[i] == "X":
                if i + 1 < len(s):
                    if s[i+1] == "L":
                        o += 40
                        i += 2
                    elif s[i+1] == "C":
                        o += 90
                        i += 2
                    else:
                        o += 10
                        i += 1
                else:
                    o += 10
                    i += 1
            elif s[i] == "C":
                if i + 1 < len(s):
                    if s[i+1] == "D":
                        o += 400
                        i += 2
                    elif s[i+1] == "M":
                        o += 900
                        i += 2
                    else:
                        o += 100
                        i += 1
                else:
                    o += 100
                    i += 1
            elif s[i] == "V":
                o += 5
                i += 1
            elif s[i] == "L":
                o += 50
                i += 1
            elif s[i] == "D":
                o += 500
                i += 1
            elif s[i] == "M":
                o += 1000
                i += 1
        return o