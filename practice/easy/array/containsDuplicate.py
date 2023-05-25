from typing import List
from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        parse = defaultdict(int)

        for num in nums:
            if parse[num] == 0:
                parse[num] += 1
            else:
                return True

        return False