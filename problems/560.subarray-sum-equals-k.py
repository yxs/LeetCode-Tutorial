from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sums = 0
        pre_sum = dict()  # 该前缀和出现的次数
        pre_sum[0] = 1  # base case
        for i in range(len(nums)):
            sums += nums[i]
            # 有几个j能够使得sum[i]和sum[j]的差为 k
            count += pre_sum.get(sums - k, 0)  # 如果有前缀和
            pre_sum[sums] = pre_sum.get(sums, 0) + 1  # 把前缀和 nums[0..i] 加入并记录出现次数
        return count


nums = [1, 2, 1, 3]
k = 3

s = Solution()
print(s.subarraySum(nums, k))

