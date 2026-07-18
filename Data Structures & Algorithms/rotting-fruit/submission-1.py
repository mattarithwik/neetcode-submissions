class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        mins = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        if fresh_count == 0:
            return 0

        while queue and fresh_count > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in ((1,0), (0, 1), (-1, 0), (0, -1)):
                    new_r = dr + r
                    new_c = dc + c

                    if (rows > new_r >= 0) and (cols > new_c >= 0) and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        fresh_count -= 1
                        queue.append((new_r, new_c))
            mins += 1

        return mins if fresh_count == 0 else -1