# 第 i 天，
# 至今最多交易 k 次，
# 1 表示持有股票

# dp
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        inf = int(1e9)
        n = len(prices)
        dp_i_0, dp_i_1 = 0, -inf
        for i in range(n):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, tmp - prices[i] - fee)

        return dp_i_0
