class Solution:
    def climbStairs(self, n: int) -> int:
        dp = dict()

        def _climb_stairs(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in dp:
                return dp[n]
            
            dp[n] = _climb_stairs(n - 1) + _climb_stairs(n - 2)
            return dp[n]
        
        return _climb_stairs(n)