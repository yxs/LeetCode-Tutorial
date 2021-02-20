class Solution:
    # func name is typo, parenthesis should be parentheses.
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(s, left, right):
            # 穷举到最后一个位置了，得到一个长度为 2n 组合
            if len(s) == 2 * n:
                ans.append("".join(s))
                return
            # 尝试放一个左括号
            if left < n:
                s.append("(")  # select
                backtrack(s, left + 1, right)
                s.pop()  # unselect
            if right < left:
                s.append(")")
                backtrack(s, left, right + 1)
                s.pop()

        backtrack([], 0, 0)
        return ans
