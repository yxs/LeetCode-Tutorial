# todo
# 可以用一种叫做快速傅立叶变换（Fast Fourier Transform，FFT）的方法来加速卷积的计算，
# 使得时间复杂度从 O(mn) 降低到 O(clogc)


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)

        ansArr = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            x = int(num1[i])
            for j in range(n - 1, -1, -1):
                ansArr[i + j + 1] += x * int(num2[j])  # i * j 的结果位于 i + j +1，进位位于 i + j

        for i in range(m + n - 1, 0, -1):
            ansArr[i - 1] += ansArr[i] // 10
            ansArr[i] %= 10

        index = 1 if ansArr[0] == 0 else 0
        ans = "".join(str(x) for x in ansArr[index:])
        return ans

