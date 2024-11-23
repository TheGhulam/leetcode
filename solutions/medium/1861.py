#Problem 1861: Rotating the Box

from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])

        for row in range(m):
            right = n - 1  # rightmost available position
            for col in range(n - 1, -1, -1):
                if box[row][col] == '#':
                    # Stone found, move it to rightmost available position
                    box[row][col] = '.'
                    box[row][right] = '#'
                    right -= 1
                elif box[row][col] == '*':
                    # Obstacle found, update rightmost available position
                    right = col - 1
        
        rotated = [['' for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated[j][m-1-i] = box[i][j]
                
        return rotated