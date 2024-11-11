#Problem 118: Pascal's Triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        
        res = [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1]
            for j in range(1, i):
                row.append(res[i-1][j-1] + res[i-1][j])
            row.append(1)
            res.append(row)
        return res

if __name__ == "__main__":
    numRows = 5
    print(Solution().generate(numRows)) # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    numRows = 1
    print(Solution().generate(numRows)) # [[1]]
    numRows = 2
    print(Solution().generate(numRows)) # [[1],[1,1]]
    numRows = 3
    print(Solution().generate(numRows)) # [[1],[1,1],[1,2,1]]