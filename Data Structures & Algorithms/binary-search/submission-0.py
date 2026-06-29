class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # Python does not overflow, but we calculate the adjusted distance as a good practice.
            mid = l + (r - l) // 2
            # Target is on the right
            if nums[mid] < target:
                l = mid + 1
            # Target is on the left
            elif nums[mid] > target:
                r = mid - 1
            # Found
            else:
                return mid
        # Not found
        return -1