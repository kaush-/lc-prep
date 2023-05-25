from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        n = n + 1
        parser = [""] * n

        for i in range(3, n, 3):
            parser[i] += "Fizz"

        for i in range(5, n, 5):
            parser[i] += "Buzz"

        for i in range(1, n):
            if parser[i] is "":
                parser[i] = str(i)

        return parser[1:]
