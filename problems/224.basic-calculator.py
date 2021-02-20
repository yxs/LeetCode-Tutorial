class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        res = 0
        sign = 1  # 1 means positive, -1 means negative
        for ch in s:
            if ch.isdigit():
                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)
            elif ch == "+":
                # Evaluate the expression to the left,
                # with result, sign, operand
                res += sign * operand
                sing = 1
                operand = 0
            elif ch == "-":
                res += sign * operand
                sing = -1
                operand = 0
            elif ch == "(":
                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif ch == ")":
                res += sign * operand
                res *= stack.pop()
                res += stack.pop()
                operand = 0
        return res + sign * operand
