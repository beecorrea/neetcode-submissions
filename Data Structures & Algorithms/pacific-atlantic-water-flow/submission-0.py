class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        def is_within_bounds(cell: tuple[int, int]) -> bool:
            return (cell[0] in range(rows)) and (cell[1] in range(cols))

        def dfs(row, col, visited, prev_height):
            cell = (row, col)
            if (cell in visited 
                or not is_within_bounds(cell)
                or not heights[row][col] >= prev_height):
                return
            
            visited.add((row, col))
            for r, c in dirs:
                dfs(row + r, col + c, visited, heights[row][col])

        # Main code
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])
        
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])
        
        return list(pacific & atlantic)

        