# Rabin-Karp 字符串哈希算法
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        # 质数 base，字符串看成一个 base 进制的数，对大质数 mod 进行取模
        base, mod = 131, 10 ** 9 + 7
        left = right = 0
        mul = 1
        best = -1

        for i in range(n):
            left = (left * base + ord(s[i])) % mod
            right = (right + mul * ord(s[i])) % mod
            if left == right:
                best = i

            mul = mul * base % mod

        add = "" if best == n - 1 else s[best + 1 :]
        return add[::-1] + s
