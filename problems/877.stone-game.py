class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True


class Solution1:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]

        for i, pile in enumerate(piles):
            dp[i][i] = pile

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])

        return dp[0][n - 1] > 0
