class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, carry, ans = len(num1) - 1, len(num2) - 1, 0, ""

        while i >= 0 or j >= 0 or carry:
            val = carry

            if i >= 0:
                i, val = i - 1, val + ord(num1[i]) - ord("0")
            if j >= 0:
                j, val = j - 1, val + ord(num2[j]) - ord("0")

            carry, val = divmod(val, 10)  # (a // b, a % b)
            ans = str(val) + ans

        return ans
