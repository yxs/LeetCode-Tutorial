# 全部除2，余下的1累加次数

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        pending = n

        for num in nums:
            if num == 0:
                pending -= 1  # 等待处理的非0字符个数

        cnt = 0
        while pending:
            for i in range(n):

                if nums[i] == 0:  # 遇到0跳过
                    continue

                a, b = divmod(nums[i], 2)
                if b == 1:
                    cnt += 1
                if a == 0:  # 某个非0字符的商成为了0
                    pending -= 1

                nums[i] = a

            cnt += 1
        return cnt - 1  # 最后退出 while 循环前多加了一次 1


nums = [7, 4, 3, 2, 0, 2]
sol = Solution()
print(sol.minOperations(nums))
