class Solution:
    def decodeString(self, s: str) -> str:
        stack, num, res = [], 0, ""
        for c in s:
            if c == "[":
                stack.append([num, res])
                num, res = 0, ""
            elif c == "]":
                curr_num, last_res = stack.pop()
                res = last_res + curr_num * res  # 拼接
            elif "0" <= c <= "9":
                num = num * 10 + int(c)  # 考虑进位
            else:
                res += c  # 存储当前字符部分
        return res


s = "aa2[abc]3[cd]ef"

sol = Solution()
print(sol.decodeString(s))
