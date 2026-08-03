class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or r >= rows or c < 0 or c >= cols or word[i] != board[r][c]):
                return False

            board[r][c] = '#'
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                new_r = dr + r
                new_c = dc + c
                if dfs(new_r, new_c, i + 1):
                    return True
            board[r][c] = word[i]
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                   if dfs(r, c, 0):
                        return True
        
        return False