class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, ocean):
            ocean.add((r, c))

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                next_r = r + dr
                next_c = c + dc

                if (0 <= next_r < rows) and (0 <= next_c < cols):
                    if (next_r, next_c) not in ocean and heights[next_r][next_c] >= heights[r][c]:
                        dfs(next_r, next_c, ocean)

        for r in range(rows):
            dfs(r, 0, pac)
            dfs(r, cols - 1, atl)
        
        for c in range(cols):
            dfs(0, c, pac)
            dfs(rows - 1, c, atl)
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r, c))
        return res