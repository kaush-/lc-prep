class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i == 0 or nums[i - 1] != nums[i]:
                lo = i + 1
                hi = len(nums) - 1

                while lo < hi:
                    val = nums[i] + nums[lo] + nums[hi]

                    if val == 0:
                        ans.append([nums[i], nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1
                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1

                    elif val > 0:
                        hi -= 1

                    else:
                        lo += 1

        return ans
