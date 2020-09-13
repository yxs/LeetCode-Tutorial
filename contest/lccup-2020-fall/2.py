# 2. 早餐组合
# https://leetcode-cn.com/contest/season/2020-fall/problems/2vYnGI/

from typing import List
from collections import Counter
from itertools import permutations, product


class Solution_TLE:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        base = 1e9 + 7
        count = 0

        if max(staple) + max(drinks) <= x:
            return int((len(staple) * len(drinks)) % base)

        combinations = map(sum, list(product(staple, drinks)))

        for combination in combinations:
            if combination <= x:
                count += 1

        return int(count % base)

        # staple[:] = [i for i in staple if i < x]
        # drinks[:] = [i for i in drinks if i < x]
        # s_staple = set(staple)
        # s_drinks = set(drinks)
        # d_staple = Counter(staple)
        # d_drinks = Counter(drinks)

        # for item1 in s_staple:
        #     for item2 in s_drinks:
        #         if item1 + item2 <= x:
        #             count += d_staple[item1] * d_drinks[item2]

        # for k1, v1 in staple.items():
        #     for k2, v2 in drinks.items():
        #         if k1 + k2 <= x:
        #             count += v1 * v2

        # for k1, v1 in staple.items():
        #     count += v1 * sum([v2 for k2, v2 in drinks.items() if k2 <= x - k1])


class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        staple.sort()
        drinks.sort()
        p = 0
        j = len(drinks) - 1
        base = 1000000007
        for i in range(len(staple)):
            while j >= 0 and drinks[j] > x - staple[i]:
                # drinks 大->小，花费超出就跳过
                j -= 1
            if j == -1:
                break
            p = (p + j + 1) % base
        return p


sol = Solution()
# staple = [10, 20, 5]
# drinks = [5, 5, 2]
# x = 15

staple = [2, 1, 1]
drinks = [8, 9, 5, 1]
x = 9
print(sol.breakfastNumber(staple, drinks, x))

