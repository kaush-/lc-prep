from typing import List
from collections import defaultdict

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        index = 0

        while index < len(nums):
            if nums[index] == 0:
                zeros += 1
                del nums[index]
                continue

            index += 1

        nums.extend([0]*zeros)