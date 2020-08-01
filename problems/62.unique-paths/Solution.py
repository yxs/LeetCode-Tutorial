# 杨辉三角
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * m
        for i in range(1, n):
            for j in range(1, m):
                # 状态转移方程为 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                # 压缩成一维数组
                dp[j] += dp[j - 1]
        return dp[-1]


m = 3
n = 3
s = Solution()
print(s.uniquePaths(m, n))
