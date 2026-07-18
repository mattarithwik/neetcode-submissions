class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        while queue:
            r, c = queue.popleft()

            for dr, dc in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                next_r = r + dr
                next_c = c + dc

                if (0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] == INF):
                    grid[next_r][next_c] = grid[r][c] + 1
                    
                    queue.append((next_r, next_c))