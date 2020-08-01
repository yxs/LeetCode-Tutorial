"""
@Date: 2020-05-03 13:56:58
@LastEditors: XueSong Ye
@LastEditTime: 2020-05-03 14:36:26
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        max_so_far = nums[0]
        max_ending_here = nums[0]
        for i in range(1, len(nums)):
            max_ending_here = max(nums[i], max_ending_here + nums[i])
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far


nums = [-1]

s = Solution()
print(s.maxSubArray(nums))
