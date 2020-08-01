"""
@Date: 2020-05-10 10:26:33
@LastEditors: XueSong Ye
@LastEditTime: 2020-05-10 10:32:05
"""
# https://leetcode-cn.com/problems/build-an-array-with-stack-operations/

from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output = []
        for i in range(1, n + 1):
            if i > target[-1]:
                break
            if i in target:
                output.append("Push")
            else:
                output.extend(["Push", "Pop"])
        return output


# target = [1, 2, 3]
# n = 3

target = [1, 3]
n = 3

# target = [1, 2]
# n = 4

# target = [2, 3, 4]
# n = 4

s = Solution()
print(s.buildArray(target, n))
