# iteratively
class Solution:
    def fib(self, N: int) -> int:
        if N == 1 or N == 2:
            return 1
        curr = 0
        prev1 = prev2 = 1
        for i in range(3, N + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return curr


# recursively
class Solution1:
    def fib(self, N: int) -> int:
        if N == 1 or N == 2:
            return 1
        return self.fib(N - 1) + self.fib(N - 2)


sol = Solution1()
print(sol.fib(4))
