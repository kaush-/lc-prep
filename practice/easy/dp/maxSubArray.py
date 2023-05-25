from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        dp = list()
        dp.append(nums[0])
        n = len(nums)

        for i in range(1, n):
            dp.append(max(dp[i - 1] + nums[i], nums[i]))
            if dp[i] > max_sum:
                max_sum = dp[i]

        return max_sum
