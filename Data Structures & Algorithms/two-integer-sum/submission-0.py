class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            diff_target = mem.get(diff)
            if diff_target != None:
                return [min(i, diff_target), max(i, diff_target)]
            
            mem[nums[i]] = i