#Problem 338: Counting Bits
#Difficulty: Easy

class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        for i in range(1, num+1):
            res.append(res[i//2] + i % 2)
        return res

if __name__ == "__main__":
    num = 2
    print(Solution().countBits(num)) # [0, 1, 1]
    num = 5
    print(Solution().countBits(num)) # [0, 1, 1, 2, 1, 2]
    num = 0
    print(Solution().countBits(num)) # [0]
    num = 1
    print(Solution().countBits(num)) # [0, 1]
    num = 10
    print(Solution().countBits(num)) # [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]