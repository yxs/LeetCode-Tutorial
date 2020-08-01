# 数字 左边乘积 乘以 右边乘积
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0] * length

        res[0] = 1
        # 计算索引 i 左侧的乘积
        for i in range(1, length):
            res[i] = nums[i - 1] * res[i - 1]

        right = 1
        for i in reversed(range(length)):
            res[i] *= right  # 左边乘以右边的值
            right *= nums[i]  # 更新右边的值

        return res
