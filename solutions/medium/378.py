#Problem 378: Kth Smallest Element in a Sorted Matrix

from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low, high = matrix[0][0], matrix[n-1][n-1]
        while low < high:
            mid = low + (high - low) // 2
            count = 0
            j = n - 1
            for i in range(n):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += j + 1
            if count < k:
                low = mid + 1
            else:
                high = mid
        return low

if __name__ == "__main__":
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    print(Solution().kthSmallest(matrix, k)) # 13
    matrix = [[-5]]
    k = 1
    print(Solution().kthSmallest(matrix, k)) # -5