from typing import List

# 1, 2, 2, 2, 3, 4


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        parse = 1
        unique_parse = 0
        curr = nums[unique_parse]

        while parse < len(nums):
            if nums[parse] != curr:
                unique_parse += 1
                nums[unique_parse] = nums[parse]
                curr = nums[parse]
            parse += 1

        return unique_parse + 1

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 2, 3, 4]
    k = sol.removeDuplicates(nums)

    print(k, nums)