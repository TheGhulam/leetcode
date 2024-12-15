#Problem 714: Best Time to Buy and Sell Stock with Transaction Fee

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        hold = [0] * n
        nothold = 0

        # Base case - day 0
        hold[0] = -prices[0] # Buy the stock

        for i in range(1, n):
            hold[i] = max(
                hold[i-1], #Keep holding
                nothold - prices[i] #Buy new stock
            )
            nothold = max(
                nothold, #Keep not holding
                hold[i-1] + prices[i] - fee #Sell stock
            )
            
        return nothold