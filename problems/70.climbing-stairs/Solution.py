class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        p, q, r = 1, 2, 0
        for i in range(3, n + 1):
            r = p + q
            p = q
            q = r
        return r
