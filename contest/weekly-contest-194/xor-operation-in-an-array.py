class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            res ^= start + 2 * i
        return res


n, start = 10, 5
sol = Solution()
print(sol.xorOperation(n, start))

