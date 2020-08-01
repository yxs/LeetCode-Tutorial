# https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies/


class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        res = []
        max_candy = max(candies)
        for i, v in enumerate(candies):
            if v + extraCandies >= max_candy:  # 现有 + 额外 >= 最大
                res.append(True)
            else:
                res.append(False)
        return res


candies = [4, 2, 1, 1, 2]
extraCandies = 1

s = Solution()
print(s.kidsWithCandies(candies, extraCandies))
