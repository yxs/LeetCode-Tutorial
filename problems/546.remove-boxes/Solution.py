# ?
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        N = len(boxes)
        memo = [[[0] * N for _ in range(N)] for _ in range(N)]

        def dp(i, j, k):
            if i > j:
                return 0
            if not memo[i][j][k]:
                m = i
                while m + 1 <= j and boxes[m + 1] == boxes[i]:
                    m += 1
                i, k = m, k + m - i  # skips order (m-i)*(j-i) calls to dp
                ans = dp(i + 1, j, 0) + (k + 1) ** 2
                for m in range(i + 1, j + 1):
                    if boxes[i] == boxes[m]:
                        ans = max(ans, dp(i + 1, m - 1, 0) + dp(m, j, k + 1))
                memo[i][j][k] = ans
            return memo[i][j][k]

        return dp(0, N - 1, 0)

