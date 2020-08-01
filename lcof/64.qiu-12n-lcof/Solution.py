# 无法使用循环和判断语句（用于终止递归时），还可以使用逻辑运算符来终止递归


class Solution:
    def __init__(self):
        self.res = 0

    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res
