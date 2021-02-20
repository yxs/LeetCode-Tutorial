class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        sign = "+"

        for i in range(len(s)):
            if s[i].isdigit():
                operand = operand * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(operand)
                elif sign == "-":
                    stack.append(-operand)
                elif sign == "*":
                    stack.append(stack.pop() * operand)
                else:
                    stack.append(int(stack.pop() / operand))
                operand = 0
                sign = s[i]
        return sum(stack)