# https://leetcode.com/problems/target-sum/discuss/804311/Python-DP-with-Comments

from typing import List

# ?
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        s = sum(nums)
        if S > s:
            return 0

        # Let dp[i][j] represent the number of possible ways to get sum j using the first i numbers.
        dp = [[0 for _ in range(s * 2 + 1)] for _ in range(len(nums))]

        dp[0][s + nums[0]] += 1
        dp[0][s - nums[0]] += 1

        for i in range(1, len(nums)):
            for j in range(s * 2 + 1):
                # make sure we don't get negative indices
                if j - nums[i] >= 0 and dp[i - 1][j - nums[i]] > 0:
                    dp[i][j] += dp[i - 1][j - nums[i]]

                if j + nums[i] <= s * 2 and dp[i - 1][j + nums[i]] > 0:
                    dp[i][j] += dp[i - 1][j + nums[i]]

        return dp[-1][S + s]


nums = [1, 1, 1, 1, 1]
S = 3

sol = Solution()

print(sol.findTargetSumWays(nums, S))
