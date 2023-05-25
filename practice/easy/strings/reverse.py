class Solution:
    def reverse(self, x: int) -> int:
        x = list(str(x))
        neg = ""
        if x[0] == "-":
            neg = x.pop(0)

        x.reverse()

        result = int("".join([neg] + x))
        return result if -2147483648 < result < 2147483647 else 0
