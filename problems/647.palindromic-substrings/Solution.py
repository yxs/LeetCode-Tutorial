# 一文让你彻底明白马拉车算法
# https://zhuanlan.zhihu.com/p/70532099

# ------

# 老司机开车，教会女朋友什么是「马拉车算法」
# https://www.cxyxiaowu.com/2665.html


# 辅助数组 `p` 的最大值就是“最长回文子串”的长度
# p 定义为回文半径「半径不计算中心」数组，半径即长度的原因是 # 等效为 double，且最边缘的 # 等效中心的字符
# 例子 @#a#b#a#$，显然半径为 3，aba 等效 #a#

# ------

# https://yuhi.xyz/post/Manacher-算法详解/
# 「半径计算中心点」~~不同分析里面定义不一样

# ------


class Solution:
    def countSubstrings(self, s: str) -> int:
        # manacher 中心扩散法
        # 插入辅助元素#，保证奇数，首尾额外插入哨兵，保证所有找到的回文串都是奇数长度的

        t = "@#" + "#".join(s) + "#$"  # 开头和结尾的两个字符一定不相等，循环就可以在这里终止

        n = len(t) - 1

        f = [0] * n  #  f[i] 来表示以 s 的第 i 位为回文中心，可以拓展出的最大回文半径「半径计算中心点」

        center, maxRight, ans = 0, 0, 0
        # maxRight 是最远的回文右半径端点
        # center 是 maxRight 对应的最左侧的回文中心

        for i in range(1, n):

            if i <= maxRight:  #  对于 i 不超出最远的回文右半径端点时

                # 初始化
                f[i] = min(maxRight - i + 1, f[2 * center - i])
                # min(到 maxRight 的距离，对称位置的回文半径)
                # i 的最大回文半径直接取其关于 center 对称的左侧镜像 f[2 * center - i]
                # 但是不能超过 maxRight，因此取 min
                # 大于 maxRight 的部分保持为 0

            # 中心拓展
            # 初始化之后 s[i + f[i] - 1 ] == s[i - f[i] + 1]
            # 暴力扩展，注意 t 加了哨兵，因此不需要考虑边界
            while t[i + f[i]] == t[i - f[i]]:
                f[i] += 1

            if i + f[i] - 1 > maxRight:  # 如果以 i 为中心的最大回文串能更新 maxRight
                center, maxRight = i, i + f[i] - 1

            ans += f[i] // 2  # 累加

        return ans


sol = Solution()

s1 = "abc"
s2 = "aaa"
s3 = "a"
s4 = "aa"
s5 = "abaa"
s6 = "abaabc"
s7 = "babad"
s8 = "abbabb"

print(sol.countSubstrings(s2))
