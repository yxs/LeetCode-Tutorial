from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0  # 最远路径，边界，步数
        for i in range(n - 1):  # 起始位置就加了一步，所以到 n-1 即可，否则如果最后一步刚好跳到了末尾，会多加一步
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos  # 更新边界
                    step += 1
        return step


nums = [2, 3, 1, 1, 4]

s = Solution()
print(s.jump(nums))
