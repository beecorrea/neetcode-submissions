class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        dp = [1] * len(nums)
        # Keep track of all LIS's.
        # At each index, look back and check if we can increase
        # the length of the subsequence.
        for i in range(len(nums)):
            # Look back:
            for j in range(i):
                # Can we increase the length?
                if nums[j] < nums[i]:
                    # Use the max between current subsequence and
                    # increased subsequence.
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

        