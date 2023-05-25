from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        while nums and nums[0] < lower:
            nums.pop(0)

        while nums and nums[-1] > upper:
            nums.pop(-1)

        if not nums:
            if lower == upper:
                return [str(lower)]
            return [str(lower) + "->" + str(upper)]

        res = []

        if nums[0] > lower:
            if nums[0] == lower + 1:
                res.append(str(lower))
            else:
                res.append(str(lower) + "->" + str(nums[0] - 1))

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                continue

            if nums[i] == nums[i - 1] + 2:
                res.append(str(nums[i] - 1))
            else:
                res.append(str(nums[i - 1] + 1) + "->" + str(nums[i] - 1))

        if nums[-1] < upper:
            if nums[-1] + 1 == upper:
                res.append(str(upper))
            else:
                res.append(str(nums[-1] + 1) + "->" + str(upper))

        return res
