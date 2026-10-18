class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Initialize rows up to query_row + 2
        arr = [[0.0] * (r + 1) for r in range(query_row + 2)]
        arr[0][0] = float(poured)

        # Distribute excess row-by-row
        for r in range(query_row + 1):
            for c in range(r + 1):
                if arr[r][c] > 1.0:
                    excess = (arr[r][c] - 1.0) / 2.0
                    arr[r + 1][c] += excess
                    arr[r + 1][c + 1] += excess
                    arr[r][c] = 1.0

        return arr[query_row][query_glass]