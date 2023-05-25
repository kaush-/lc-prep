# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        last = n
        first = 1
        middle = (first + last) // 2

        while middle < last:
            if isBadVersion(middle):
                if middle == first:
                    return middle

                if not isBadVersion(middle - 1):
                    return middle

                last = middle
                middle = (first + last) // 2
                continue

            first = middle + 1
            middle = (first + last) // 2

        return middle
