class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = int(1e9)
        n = len(prices)
        dp_i_0, dp_i_1 = 0, -inf
        dp_pre_0 = 0  # 代表 dp[i-2][0]，从i-2开始转移
        for i in range(n):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = tmp

        return dp_i_0
