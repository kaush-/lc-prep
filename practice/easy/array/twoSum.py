from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}

        for i in range(len(nums)):
            if target - nums[i] in myDict.keys():
                return [myDict[target - nums[i]], i]
            myDict[nums[i]] = i

