from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [item + [num] for item in res]
        return res


s = Solution()
nums = [1, 2, 3]
print(s.subsets(nums))
