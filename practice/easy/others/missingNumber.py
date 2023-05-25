from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        parse = list(range(n))

        for num in nums:
            parse[num] = 0

        return sum(parse)
