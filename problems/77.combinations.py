import itertools


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))


# 区别于普通回溯，字典序法
class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 将 temp 中 [0, k - 1] 每个位置 i 设置为 i + 1，即 [0, k - 1] 存 [1, k]
        # 末尾加一位 n + 1 作为哨兵
        temp = [i for i in range(1, k + 1)]
        temp.append(n + 1)
        ans = []
        j = 0
        # 寻找第一个 temp[j] + 1 != temp[j + 1] 的位置 t
        # 我们需要把 [0, t - 1] 区间内的每个位置重置成 [1, t]
        while j < k:
            ans.append(temp[:k])
            j = 0
            while j < k and temp[j] + 1 == temp[j + 1]:
                temp[j] = j + 1
                j += 1

            # j 是第一个 temp[j] + 1 != temp[j + 1] 的位置
            temp[j] += 1
        return ans
