#Problem 6: ZigZag Conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): return s
        
        n = len(s)
        cycle = 2 * numRows - 2
        o = [] 

        for i in range(0, n, cycle):
            o.append(s[i])

        for r in range(1, numRows-1):
            for i in range(r, n, cycle):
                o.append(s[i])
                second_idx = i + cycle - 2*r
                if second_idx < n:
                    o.append(s[second_idx])

        for i in range(numRows-1, n, cycle):
            o.append(s[i])

        return ''.join(o)


class Solution:
    def convert(s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [[] for _ in range(numRows)]
        current_row = 0
        step = 1  # 1 means moving down, -1 means moving up
        
        for char in s:
            rows[current_row].append(char)
            
            if current_row == numRows - 1:
                step = -1
            elif current_row == 0:
                step = 1
                
            current_row += step
        
        return ''.join([''.join(row) for row in rows])