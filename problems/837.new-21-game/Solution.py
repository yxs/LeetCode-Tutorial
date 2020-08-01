# https://leetcode-cn.com/problems/new-21-game/
# 没整明白


class Solution:
    # 不少于 K 分停止，每次加 1~W，求不超过 N 分概率
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1.0
        dp = [0.0] * (K + W + 1)
        for i in range(K, min(N, K + W - 1) + 1):  # K - 1 + W 不能超过 N
            dp[i] = 1.0
        dp[K - 1] = float(min(N - K + 1, W)) / W
        for i in range(K - 2, -1, -1):
            # dp 相邻项计算差分得出
            dp[i] = dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / W
        return dp[0]


N = 21
K = 17
W = 10
sol = Solution()
print(sol.new21Game(N, K, W))
