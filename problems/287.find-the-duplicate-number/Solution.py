# 本题有如下限制条件：
# 1. 不能更改原数组 2. 只能使用额外的 O(1) 的空间
# 否则，常用解法为哈希或者排序


# 还可以妙用快慢指针
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        left = 1
        right = size - 1

        while left < right:
            mid = left + (right - left) // 2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt > mid:
                right = mid  # 目标在左边
            else:
                left = mid + 1
        return left
