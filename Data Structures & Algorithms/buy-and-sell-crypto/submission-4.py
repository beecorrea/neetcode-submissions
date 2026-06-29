class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # The idea here is to buy at the lowest price 
        # and sell at the highest price.

        # DP solution
        # We keep track of the sell candidate, and if we find
        # a better candidate we update it.
        lowest = prices[0]
        profit = 0

        for p in prices:
            profit = max(profit, p - lowest)
            lowest = min(lowest, p)

        return profit