"""
@Date: 2020-05-13 11:25:19
@LastEditors: XueSong Ye
@LastEditTime: 2020-05-13 11:52:05
"""


def permutations(nums):
    def backtrack(first=0):
        if first == n:
            res.append(nums[:])
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)
    res = []
    backtrack()
    return res


nums = [2, 3, 1, 3]
print("\n".join(map(str, permutations(sorted(set(nums))))))
