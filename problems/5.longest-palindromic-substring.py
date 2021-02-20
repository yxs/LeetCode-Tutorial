# 回文，亦称回环，是正读反读都能读通的句子
class Solution1:
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


# Manacher 算法，没有完全理解
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        t = "#"  # 插入分割符
        for i in range(size):
            t += s[i]
            t += "#"

        t_len = 2 * size + 1
        p = [0 for _ in range(t_len)]

        max_right = 0  # 当前向右扩展的最远边界
        center = 0  # 回文串的中心

        max_len = 1
        start = 1

        for i in range(t_len):
            if i < max_right:
                mirror = 2 * center - i  # mirror 为 i 关于 center 对称的点
                p[i] = min(max_right - i, p[mirror])
            left = i - (1 + p[i])
            right = i + (1 + p[i])

            while left >= 0 and right < t_len and t[left] == t[right]:
                p[i] += 1
                left -= 1
                right += 1

            if i + p[i] > max_right:
                max_right = i + p[i]
                center = i
            if p[i] > max_len:
                max_len = p[i]
                start = (i - max_len) // 2

        return s[start : start + max_len]


sol = Solution()
s = "babad"
print(sol.longestPalindrome(s))
