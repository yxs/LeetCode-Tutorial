# 一次遍历，一次买，一次卖，找最大差值
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        inf = int(1e9)
        minPrice = inf  # 最低价取极大值
        maxProfit = 0
        for price in prices:
            maxProfit = max(price - minPrice, maxProfit)  # 最大利润和（当前价格 - 最低价）中取大者
            minPrice = min(price, minPrice)  # 更新最低价
        return maxProfit


# 第 i 天，
# 至今最多交易 k 次，
# 1 表示持有股票

# dp
# k=1，降成2维
# 再优化成1维
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = int(1e9)
        n = len(prices)
        # dp[-1][0] = 0, dp[-1][1] = -infinity
        dp_i_0, dp_i_1 = 0, -inf
        for i in range(n):
            # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            # dp[i][1] = max(dp[i-1][1], -prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        
        return dp_i_0
