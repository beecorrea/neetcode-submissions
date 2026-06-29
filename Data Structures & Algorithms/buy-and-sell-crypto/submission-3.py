class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # The idea here is to buy at the lowest price 
        # and sell at the highest price.
        # We keep track of the buy candidate, and if we find
        # a better candidate we update it.

        # Optimized: sliding window.
        left, right = 0, 1
        profit = 0
        while right < len(prices):
            # Try to find lower value to buy.
            if prices[right] > prices[left]:
                profit = max(profit, prices[right] - prices[left])
            else:
                left = right
            right += 1


        return profit