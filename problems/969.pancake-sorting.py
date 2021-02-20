from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for x in range(len(arr), 1, -1):
            i = arr.index(x)  # 先找到最大的元素的索引
            res.extend([i + 1, x])  # 反转最大值及前面的部分+整个翻转
            arr = arr[:i:-1] + arr[:i]  # i后倒序的+i前面的值，两次反转后的子数组(除去最大值)的状态
        return res


arr = [3, 2, 4, 1]
s = Solution()
print(s.pancakeSort(arr))
