class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k > n / 2:
            inf = int(1e9)
            n = len(prices)
            dp_i_0, dp_i_1 = 0, -inf
            for i in range(n):
                tmp = dp_i_0
                dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
                dp_i_1 = max(dp_i_1, tmp - prices[i])

            return dp_i_0

        max_k = k
        dp = [[[0] * 2 for _ in range(max_k + 1)] for _ in range(n)]
        for i in range(n):
            for k in range(max_k, 0, -1):
                if i - 1 == -1:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[n - 1][max_k][0]
