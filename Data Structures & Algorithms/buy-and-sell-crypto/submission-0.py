class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # The idea here is to buy at the lowest price 
        # and sell at the highest price.
        # We keep track of the buy candidate, and if we find
        # a better candidate we update it.

        profit = 0
        # Brute force: check for every value.
        for buy in range(len(prices)):
            for sell in range(buy + 1, len(prices)):
                cand = prices[sell] - prices[buy]
                profit = max(profit, cand)

        return profit
