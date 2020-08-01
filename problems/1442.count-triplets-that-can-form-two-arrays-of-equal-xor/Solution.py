"""
@Date: 2020-05-10 10:26:40
@LastEditors: XueSong Ye
@LastEditTime: 2020-05-10 11:36:44
"""

from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        cnt = 0
        res = []
        for i in range(len(arr) - 1):
            for j in range(len(arr) - 1):
                for k in range(len(arr)):
                    if i < j <= k:
                        if (
                            arr[i] ^ arr[i + 1] ^ arr[j - 1]
                            == arr[j] ^ arr[j + 1] ^ arr[k]
                        ):
                            res.append([i, i + 1, j - 1])
                            cnt += 1
        return res, cnt


s = Solution()

print(s.countTriplets([2, 3, 1, 6, 7]))
