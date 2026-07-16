class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c) -> int:
            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(dfs(r, c), max_area)
        
        return max_area