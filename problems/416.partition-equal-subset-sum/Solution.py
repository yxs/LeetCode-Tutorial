class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        # 不到两个
        if n < 2:
            return False

        total = sum(nums)
        maxNum = max(nums)
        # 和为奇数
        if total & 1:
            return False

        target = total // 2
        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]

        return dp[target]
