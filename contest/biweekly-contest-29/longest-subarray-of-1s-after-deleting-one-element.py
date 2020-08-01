from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if sum(nums) == n:
            return n - 1
        ans = 0
        for i in range(n):
            if nums[i] == 1:
                continue
            L = R = i
            # 巧妙的以单个的 0 为中心，往两边扩展，而左右两端的差值，是长度 - 1，但是由于要排除 0，所以直接 R - L 即可，妙啊！
            while L - 1 >= 0 and nums[L - 1] == 1:
                L -= 1
            while R + 1 < n and nums[R + 1] == 1:
                R += 1
            ans = max(ans, R - L)
        return ans


nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]

sol = Solution()
print(sol.longestSubarray(nums))
