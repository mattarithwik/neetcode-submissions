class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()


        def dfs(r, c):
            nonlocal perimeter
            visited.add((r, c))

            for dr, dc in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                new_r = dr + r
                new_c = dc + c

                if (new_r, new_c) in visited:
                    continue

                if new_r >= rows or new_r < 0 or new_c < 0 or new_c >= cols:
                    perimeter += 1
                    continue
                
                if grid[new_r][new_c] == 0:
                    perimeter += 1
                    continue

                dfs(new_r, new_c)



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return perimeter

        return 0