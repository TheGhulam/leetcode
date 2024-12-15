#Problem 765: Couples Holding Hands

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        res = 0

        # Store the position of each couple
        pos = {}
        for i, c in enumerate(row):
            pos[c] = i

        # Iterate through the row by pairs
        for i in range(0, n, 2):
            c = row[i]
            p = c + 1 if c % 2 == 0 else c - 1

            if row[i+1] != p:
                p_pos = pos[p]
                row[i+1], row[p_pos] = row[p_pos], row[i+1]
                pos[row[i+1]] = i + 1
                pos[row[p_pos]] = p_pos 
                res += 1
        
        return res