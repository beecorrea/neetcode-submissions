class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Take advantage of the fact that numbers are sorted ascending.
        # The numbers list is essentially split into big and small parts.
        # Left pointer looks for small element, right pointer looks for big element.
        # Return [left+1, right+1] at the end to convert to 1-indexing.
 
        # numbers = [1, 2, 4, 5, 6], target = 9
        l, r = 0, len(numbers) - 1

        while l < r:
            if target > numbers[l] + numbers[r]:
                l += 1
            elif target < numbers[l] + numbers[r]:
                r -= 1
            else:
                return [l+1, r+1]        
        # while target < numbers[l] + numbers[r]:
        
        return [l+1, r+1]