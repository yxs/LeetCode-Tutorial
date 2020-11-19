class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == ".":
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    # 不匹配字符，将该组合扔掉，不再进行匹配
                    # 'c*' 匹配完 'c' 之后，把 'c*' 丢弃
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        # 'c*' 匹配完 'c' 之后，继续发挥作用
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        # .
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]

# https://leetcode-cn.com/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode-solution/452279
