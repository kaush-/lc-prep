from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        z_rows = set()
        z_cols = set()

        n_rows = len(matrix)
        n_cols = len(matrix[0])

        for i in range(n_rows):
            for j in range(n_cols):
                if matrix[i][j] == 0:
                    z_rows.add(i)
                    z_cols.add(j)

        for row in z_rows:
            for j in range(n_cols):
                matrix[row][j] = 0

        for col in z_cols:
            for i in range(n_rows):
                matrix[i][col] = 0
