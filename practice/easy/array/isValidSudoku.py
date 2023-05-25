from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            check_row_data = [x for x in board[i] if x != "."]
            check_col_data = [x for x in [row[i] for row in board] if x != "."]

            row_add = (i // 3) * 3
            col_add = (i % 3) * 3
            check_block_data = []
            for row in range(3):
                for col in range(3):
                    if board[row + row_add][col + col_add] != ".":
                        check_block_data.append(board[row + row_add][col + col_add])

            if len(check_row_data) != len(set(check_row_data)) or len(check_col_data) != len(set(check_col_data))\
                    or len(check_block_data) != len(set(check_block_data)):
                return False

        return True
