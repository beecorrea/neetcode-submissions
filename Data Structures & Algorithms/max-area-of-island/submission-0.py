class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    # This is like number of islands, except you have to
    # recompute the maximum island after each BFS.
        directions = [[-1,0], [1, 0], [0, 1], [0, -1]]

        def is_within_bounds(r, c) -> bool:
            return (
                r in range(len(grid)) and
                c in range(len(grid[0]))
            )

        visited = set()
        max_area = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r, c))
            area = 1

            while q:
                row, col = q.popleft()
                for dir_row, dir_col in directions:
                    cell_row = row + dir_row
                    cell_col = col + dir_col

                    if (is_within_bounds(cell_row, cell_col)
                        and grid[cell_row][cell_col] == 1
                        and (cell_row, cell_col) not in visited):
                        
                        area += 1
                        visited.add((cell_row, cell_col))
                        q.append((cell_row, cell_col))
            
            return area

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, bfs(r, c))

        return max_area
                    

