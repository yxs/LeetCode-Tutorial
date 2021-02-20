# https://leetcode-cn.com/problems/valid-parentheses/
# leetcode 20

# 本题还可以写成 list.append() + list.pop() 直接比对，显然利用 dict 更加简洁


class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"{": "}", "[": "]", "(": ")", "?": "?"}  # ? 防止栈空 pop
        stack = ["?"]
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1


s = "(){[]}"

sol = Solution()
print(sol.isValid(s))
