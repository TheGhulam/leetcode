#Problem 1833: Maximum Ice Cream Bars

from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        minv, maxv = min(costs), max(costs)
        r = maxv - minv + 1

        cnt = [0] * r
        for c in costs:
            cnt[c-minv] += 1

        s = 0
        c = 0
        for i in range(r):
            while cnt[i] > 0 and s + (i + minv) < coins:
                s += i + minv
                c += 1
                cnt[i] -= 1
        
        return c
        
if __name__ == "__main__":
    solution = Solution()

    # Expected: 4
    print(solution.maxIceCream([1,3,2,4,1], 7))

    # Expected: 0
    print(solution.maxIceCream([10,6,8,7,7,8], 5))

    # Expected: 6
    print(solution.maxIceCream([1,6,3,1,2,5], 20))
