# 回文，亦称回环，是正读反读都能读通的句子


class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s
        dp = [[False for _ in range(size)] for _ in range(size)]

        max_len = 1
        start = 0

        for i in range(size):
            dp[i][i] = True

        for j in range(1, size):
            for i in range(j - 1, -1, -1):
                if s[i] == s[j]:
                    if j - i < 3:  # 子串长度为 2 或 3
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1  # 记录回文长度
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i  # 记录起始位置

        return s[start : start + max_len]
