# Problem 70: Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b = 1, 2
        for i in range(3, n+1):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    n = 5

    solution = Solution()

    result = solution.climbStairs(n)
    print(f"Number of ways to climb {n} stairs: {result}")
    print()