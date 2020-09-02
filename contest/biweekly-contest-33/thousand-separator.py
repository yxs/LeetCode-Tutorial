class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = ""
        if n == 0:
            return str(n)
        while n > 1000:
            n, sub = divmod(n, 1000)
            s = "." + str(format(sub, '03d')) + s
        s = str(n) + s
        return s

sol = Solution()
n1 = 123456789
n2 = 51040
print(sol.thousandSeparator(n2))