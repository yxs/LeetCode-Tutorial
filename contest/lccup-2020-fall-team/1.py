# https://leetcode-cn.com/problems/ccw6C7/


# 清晰思路
# https://leetcode-cn.com/problems/ccw6C7/solution/shu-xue-tui-dao-by-sunrise-z/


class Solution1:
    def paintingPlan(self, n: int, k: int) -> int:
        if k in (0, n * n):
            return 1

        def get(n, a):
            # 计算组合公式迭代版
            # 组合数公式 n! / (r! * ( n - r )!)
            res = 1
            for i in range(n, n - a, -1):
                res *= i  # res = n ~ n-r 的乘积
            for j in range(1, a + 1):
                res /= j  # res / r!

        ans = 0
        for i in range(n):
            for j in range(n):
                if n * (i + j) - (i * j) == k:  # 所有的行数和列数 - 交叉重复
                    ans += get(n, i) * get(n, j)
        return int(ans)


# @whzzt 的解法
class Solution:
    def paintingPlan(self, n: int, k: int) -> int:
        if k == 0 or k == n * n:
            return 1

        # 这段代码的原理是什么？怎么和组合搭上关系的
        # 杨辉三角 https://zh.wikipedia.org/zh-cn/杨辉三角形

        # https://zhenghao-liu.blog.luogu.org/pai-lie-zu-ge-shuo

        bin = [[0 for i in range(n + 1)] for i in range(n + 1)]
        for i in range(n + 1):
            bin[i][0] = 1  # 第一列赋值
            for j in range(1, i + 1):
                # 主对角线及下半部分，值为斜上方 + 上方，杨辉三角的性质
                # https://zh.wikipedia.org/zh-cn/帕斯卡法则
                bin[i][j] = bin[i - 1][j - 1] + bin[i - 1][j]

        # print(bin)
        # [[1, 0, 0, 0], [1, 1, 0, 0], [1, 2, 1, 0], [1, 3, 3, 1]]

        cnt = 0
        for l in range(n):
            for r in range(n):
                if (n - l) * (n - r) == n * n - k:  # 所有的行数和列数 - 交叉重复
                    cnt += bin[n][l] * bin[n][r]

        return cnt


n = 3
k = 5
solution = Solution()
print(solution.paintingPlan(n, k))

