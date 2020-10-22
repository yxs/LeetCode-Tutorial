# https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/zui-xiao-cha-ru-hui-wen


class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        tmp = 0
        # base case：i == j 时 dp[i][j] = 0
        dp = [0] * n

        for i in range(n - 2, -1, -1):
            pre = 0
            for j in range(i + 1, n):
                # https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/zhuang-tai-ya-suo-ji-qiao
                tmp = dp[j]

                if s[i] == s[j]:
                    dp[j] = pre
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + 1

                pre = tmp

        return dp[n - 1]


s = "leetcode"

sol = Solution()

print(sol.minInsertions(s))

