# 3. 秋叶收藏集


# 常规解法 @acst
class Solution:
    def minimumOperations(self, leaves: str) -> int:
        basics = 0
        # 处理边界
        if leaves[0] == "y":
            basics += 1
            leaves = "r" + leaves[1:]
        if leaves[-1] == "y":
            basics += 1
            leaves = leaves[:-1] + "r"
        ints = []
        s = 1

        # 记录相同连续相同字段的 list
        for i in range(1, len(leaves)):
            if leaves[i] != leaves[i - 1]:
                ints.append(s)
                s = 1
            else:
                s += 1
        ints.append(s)

        ro, r, y = [], [], []
        for i in range(1, len(ints), 2):
            if i == 1:
                ro.append(ints[i])
                r.append(ints[i])
                y.append(0)
            else:
                ro.append(ro[-1] + ints[i])
                r.append(min(ro[-2] + ints[i], r[-1] + ints[i], y[-1] + ints[i]))
                y.append(min(ro[-2], y[-1] + ints[i - 1]))
        if not y:
            k = 1
        else:
            k = min(y[-1], ro[-1] - 1, r[-1])
        return k + basics


# @汪乐平 的简洁解法
# ？？？ TODO
class Solution_W:
    def minimumOperations(self, leaves: str) -> int:
        s = [0 for _ in range(100005)]
        n = len(leaves)
        ans = n
        # 第一个循环，s 记录累计到当前的 y 的个数，从 1 开始记录
        for i in range(n):
            s[i + 1] = s[i] + (leaves[i] == "y")
        for i in range(1, n):
            s[i] = i - 2 * s[i]
        j = s[1]
        for i in range(2, n):
            ans = min(ans, s[n] + s[i] - j)
            j = max(j, s[i])
        return ans


sol = Solution()
leaves = "rrryyyrryyyrr"
print(sol.minimumOperations(leaves))
