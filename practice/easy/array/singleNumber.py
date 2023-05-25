from typing import List
from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        parse = defaultdict(int)

        for num in nums:
            parse[num] += 1

        for key, value in parse.items():
            if value == 1:
                return key