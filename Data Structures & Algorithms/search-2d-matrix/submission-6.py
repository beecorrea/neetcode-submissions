class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Strategy: find the correct row, then find the correct column
        # Use binary search for each search
        # Time complexity: O(log(m) + log(n)) (m binary searches then n binary searches)
        # Space complexity: O(1)
        rows, cols = len(matrix), len(matrix[0])
        up, down = 0, rows - 1
        r = 0
        while up <= down:
            mid = up + (down - up) // 2
            print(mid, up, down)
            if matrix[mid][-1] < target:
                up = mid + 1
            elif matrix[mid][0] > target:
                down = mid - 1
            else:
                r = mid 
                break
        
        left, right = 0, cols-1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[r][mid] < target:
                left = mid + 1
            elif matrix[r][mid] > target:
                right = mid - 1
            else:
                return True
        
        return False
                