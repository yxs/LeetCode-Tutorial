# s 是否是 t 的子序列?
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        # f[i][j] 表示字符串 t 中从位置 i 开始往后字符 j 第一次出现的位置
        f = [[0] * 26 for _ in range(m)]
        f.append([m] * 26)

        for i in range(m - 1, -1, -1):
            for j in range(26):
                f[i][j] = i if ord(t[i]) == j + ord("a") else f[i + 1][j]

        add = 0
        for i in range(n):
            if f[add][ord(s[i]) - ord("a")] == m:
                return False
            add = f[add][ord(s[i]) - ord("a")] + 1

        return True


s = "abc"

t = "ahbgdc"

sol = Solution()
print(sol.isSubsequence(s, t))
