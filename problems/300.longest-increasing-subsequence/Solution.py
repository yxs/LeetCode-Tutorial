from typing import List

class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                # 新加入的大于之前的
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #  d[i] ，表示长度为 i 的最长上升子序列的末尾元素的最小值
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1

                d[loc] = n

        return len(d)


nums = [10, 9, 2, 5, 3, 7, 101]

sol = Solution1()

print(sol.lengthOfLIS(nums))