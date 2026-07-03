class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Problem is pretty much multiple BFS that 
        # halt when the a cell is "0".
        # Time Complexity: O(rows * cols) (have to visit every cell)
        # Space Complexity: O(rows * cols) (visited set + counter variable).

        # up: [-1, 0], right: [0, 1], down: [1, 0], left: [0, -1].
        directions = [[-1,0], [0, 1], [1, 0], [0, -1]]
        num_islands = 0
        if not grid:
            return num_islands
        
        # Iterate over the grid.
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dir_row, dir_col in directions:
                    vec_row = row + dir_row
                    vec_col = col + dir_col

                    # Visit conditions (in order): 
                    # - Within bounds
                    # - Is land cell
                    # - Not visited
                    if (vec_row in range(rows) and 
                        vec_col in range(cols) and 
                        grid[vec_row][vec_col] == "1" and
                        (vec_row, vec_col) not in visited):
                        
                        q.append((vec_row, vec_col))
                        visited.add((vec_row, vec_col))


        for r in range(rows):
            for c in range(cols):
                # Is an island and hasn't visited yet.
                if grid[r][c] == "1" and (r, c) not in visited:
                    # Run a BFS to visit all cells of that island.
                    bfs(r, c)
                    num_islands += 1
        
        return num_islands

