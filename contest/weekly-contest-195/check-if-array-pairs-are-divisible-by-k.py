from typing import List
from collections import Counter


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        c = Counter()
        for x in arr:
            c[x % k] += 1  # 得到每种余数情况的 dict
        if c[0] % 2 != 0:  # array 中数本身可以整数的个数必须为偶数
            return False
        for i in range(1, k):
            if c[i] != c[k - i]:  # 配对
                return False
        return True


arr = [-1, 1, -2, 2, -3, 3, -4, 4]
k = 3
sol = Solution()
print(sol.canArrange(arr, k))
