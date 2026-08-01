class Solution:
    def rob(self, nums: List[int]) -> int:
        # Let's say that these are the houses:
        #   [6, 3, 12, 9, 4]
        # Alternative 1:
        #   We could compute all amounts of money and
        #   choose the best solution.
        #   Two passes + auxiliary array = O(n) / O(n)
        # Alternative 2:
        #   If you pick an even house, you can only pick even houses.
        #   If you pick an odd house, you can only pick odd houses.
        #   Q: Do you have to rob every house?
        dp = [-1] * len(nums)
        def _rob(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            # Current choice is the max between 
            # robbing the current house or skipping it.
            dp[i] = max(nums[i] + _rob(i + 2), _rob(i + 1))
            return dp[i]
        
        return _rob(0)
