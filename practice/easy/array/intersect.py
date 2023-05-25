from typing import List
from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        parse = defaultdict(int)
        result = []

        for num in nums1:
            parse[num] += 1

        for num in nums2:
            if parse[num] > 0:
                result.append(num)
                parse[num] -= 1

        return result