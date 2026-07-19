class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            board[r][c] = 'A'
            visited.add((r, c))
            for dr, dc in [(1,0), (0, -1), (-1,0), (0,1)]:
                new_r = dr + r
                new_c = dc + c
                
                if (0 <= new_r < rows) and (0 <= new_c < cols) and (new_r, new_c) not in visited and board[new_r][new_c] != 'X':
                    dfs(new_r, new_c)


        for r in range(rows):
            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)
            if board[r][0] == 'O':
                dfs(r, 0)
        
        for c in range(cols):
            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)
            if board[0][c] == 'O':
                dfs(0, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'A':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
                
        
        
