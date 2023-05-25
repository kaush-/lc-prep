import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        log_res = int(math.ceil(math.log(n, 3)))

        return 3 ** log_res == n
