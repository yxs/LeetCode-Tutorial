"""
@Date: 2020-05-05 18:25:08
@LastEditors: XueSong Ye
@LastEditTime: 2020-05-05 20:22:30
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res
