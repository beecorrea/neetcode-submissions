class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = dict()
        def _lis(i):
            if i == len(nums) - 1:
                return 1
            if i in dp:
                return dp[i]    
            
            res = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    res = max(res, 1 + _lis(j))
            dp[i] = res

            return dp[i]
        
        max_res = _lis(0)
        for i in range(1, len(nums)):
            max_res = max(max_res, _lis(i))
        
        return max_res
