from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 左指针左边均为非零数
        # 右指针左边直到左指针处均为零
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


nums = [0, 1, 0, 3, 12]

s = Solution()
s.moveZeroes(nums)
