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
        center = 0 # 回文串的中心

        max_len = 1
        start = 1

        for i in range(t_len):
            if i < max_right:
                mirror = 2 * center - i # mirror 为 i 关于 center 对称的点
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
