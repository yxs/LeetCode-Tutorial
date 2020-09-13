# 1. 速算机器人


class Solution:
    def calculate(self, s: str) -> int:
        x, y = 1, 0
        for num in s:
            if num == "A":
                x = 2 * x + y
            if num == "B":
                y = 2 * y + x
        return x + y


sol = Solution()
s = "AB"
print(sol.calculate(s))
