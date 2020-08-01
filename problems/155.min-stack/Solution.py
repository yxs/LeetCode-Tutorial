"""
@Date: 2020-05-12 12:32:31
@LastEditors: XueSong Ye
@LastEditTime: 2020-05-12 13:23:05
"""
import math

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

        # 辅助栈和数据栈不同步
        # 出栈时，最小值出栈才同步；入栈时，最小值入栈才同步。

        # if len(self.min_stack) == 0 or x <= self.min_stack[-1]:
        #     self.min_stack.append(x)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

        # top = self.stack.pop()
        # if self.min_stack and top == self.min_stack[-1]:
        #     self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
