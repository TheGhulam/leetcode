#Problem 807: Max Increase to Keep City Skyline

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Find maximum height in each row (for East/West skyline)
        row_maxes = [max(row) for row in grid]
        
        # Find maximum height in each column (for North/South skyline)
        col_maxes = [max(col) for col in zip(*grid)]
        
        total_increase = 0
        
        for i in range(n):
            for j in range(n):
                new_height = min(row_maxes[i], col_maxes[j])
                total_increase += new_height - grid[i][j]
        
        return total_increase