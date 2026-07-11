class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)  # Number of rows
        cols = len(matrix[0])  # Number of columns

        left = 0
        right = (rows * cols) - 1

        while left <= right:
            mid = left + (right - left) // 2

            row = mid // cols
            col = mid % cols

            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
