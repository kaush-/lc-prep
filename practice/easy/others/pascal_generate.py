from collections import defaultdict
from math import comb
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        memo_comb = defaultdict(int)

        for i in range(1, numRows):
            row_result = []
            for j in range(0, i + 1):
                if memo_comb[(i, j)] == 0:
                    memo_comb[(i, j)] = comb(i, j)
                    memo_comb[(i, i - j)] = memo_comb[(i, j)]

                row_result.append(memo_comb[(i, j)])

            result.append(row_result)

        return result
