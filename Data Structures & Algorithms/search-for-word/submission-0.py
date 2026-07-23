class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = set()
        def is_within_bounds(cell: tuple[int, int]) -> bool:
            return (cell[0] in range(rows)) and (cell[1] in range(cols))

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            
            if (not is_within_bounds((r, c))
                or (r, c) in visited
                or word[idx] != board[r][c]):
                return False
            
            visited.add((r, c))
            res = False
            for row, col in dirs:
                res = res or dfs(r + row, c + col, idx + 1)
            visited.remove((r, c))

            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False
