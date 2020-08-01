# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = int(1e9)
        minPrice = inf  # 最低价取极大值
        maxProfit = 0
        for price in prices:
            maxProfit = max(price - minPrice, maxProfit)  # 最大利润和（当前价格 - 最低价）中取大者
            minPrice = min(price, minPrice)  # 更新最低价
        return maxProfit
