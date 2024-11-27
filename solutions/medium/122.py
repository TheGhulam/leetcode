#Problem 122: Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0

        # "you can buy it then immediately sell it on the same day."
        # Can use a greedy approach capturing daily price diff
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                p += prices[i]-prices[i-1]
        return p