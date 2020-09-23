# https://leetcode-cn.com/problems/er94lq/


from typing import List

# 这就是暴力解法，我为什么比赛时TLE？题都搞错了，没有关系 K 的取值。
# https://leetcode-cn.com/submissions/detail/109552345/


# @风自西来毛则东 详细推理分析 https://leetcode-cn.com/problems/er94lq/solution/mo-ni-xi-pai-guo-cheng-xiang-xi-fen-xi-li-jie-kde-/


class Solution:
    def isMagic(self, target: List[int]) -> bool:
        n = len(target)

        # 第一次洗牌，下标从 1 开始，偶数位置放前面
        a = [i for i in range(2, n + 1, 2)]
        a.extend([i for i in range(1, n + 1, 2)])

        # 记录第一次洗牌后与 target 开始不匹配的位置，推理可得 k == 公共前缀长
        k = n
        for i in range(n):
            if a[i] != target[i]:
                k = i
                break

        if not k:
            return False

        for i in range(n):
            a[i] = i + 1

        ans = []
        while a:
            # 偶数位置放到前面
            b = [a[i] for i in range(1, len(a), 2)]
            b.extend([a[i] for i in range(0, len(a), 2)])
            a.clear()

            for i in range(len(b)):
                if i < k:
                    ans.append(b[i])
                else:
                    a.append(b[i])

        return target == ans


target = [2, 4, 3, 1, 5]
sol = Solution()
print(sol.isMagic(target))
