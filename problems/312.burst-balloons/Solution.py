class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        # base case 初始化
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        val = [1] + nums + [1]

        # i 从下往上
        for i in range(n - 1, -1, -1):
            # j 从左到右
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    dp[i][j] = max(
                        dp[i][j], dp[i][k] + dp[k][j] + val[i] * val[j] * val[k]
                    )

        return dp[0][n + 1]
