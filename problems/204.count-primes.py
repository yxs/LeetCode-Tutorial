# Sieve of Eratosthenes
# O(nloglogn)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0

        # 由于因子的对称性，只需要计算到根号n
        for i in range(2, int(n ** 0.5) + 1):
            # 还未赋值为0
            if isPrime[i]:
                # 考虑到数与数的关联性
                # 将其所有的倍数都标记为合数
                # 切片赋值
                isPrime[i * i : n : i] = [0] * ((n - 1 - i * i) // i + 1)

        return sum(isPrime)


n = 100
s = Solution()
print(s.countPrimes(n))