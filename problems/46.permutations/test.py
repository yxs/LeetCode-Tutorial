"""
@Date: 2020-05-14 17:43:08
@LastEditors: XueSong Ye
@LastEditTime: 2020-05-14 17:43:08
"""

# by liweiwei1419


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path[:])
                return

            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    dfs(nums, size, depth + 1, path, used, res)
                    # 注意：这里是状态重置，是从深层结点回到浅层结点的过程，代码在形式上和递归之前是对称的
                    used[i] = False
                    path.pop()

        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False for _ in range(size)]
        res = []
        dfs(nums, size, 0, [], used, res)
        return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    res = solution.permute(nums)
    print(res)
