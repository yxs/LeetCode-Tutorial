# 滑动窗口 1 2 3

# 子串逐一比较 - 线性时间复杂度
class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        h, n = len(haystack), len(needle)

        for start in range(h - n + 1):
            if haystack[start : start + n] == needle:
                return start
        return -1


# 双指针 - 线性时间复杂度
class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        h, n = len(haystack), len(needle)
        if n == 0:
            return 0
        ph = 0
        while ph < h - n + 1:
            # haystack 中查找 needle 的第一个字符
            while ph < h - n + 1 and haystack[ph] != needle[0]:
                ph += 1
            curr_len = pn = 0
            # 找到当前最长能匹配的字符串
            while ph < h and pn < n and haystack[ph] == needle[pn]:
                ph += 1
                pn += 1
                curr_len += 1

            # 找到needle
            if curr_len == n:
                return ph - n

            ph = ph - curr_len + 1

        return -1


# Rabin Karp - 常数复杂度
class Solution3:
    def strStr(self, haystack: str, needle: str) -> int:
        h, n = len(haystack), len(needle)
        if n > h:
            return -1

        # base value for the rolling hash function
        a = 26
        # modulus value for the rolling hash function to avoid overflow
        modulus = 2 ** 31

        h_to_int = lambda i: ord(haystack[i]) - ord("a")
        needle_to_int = lambda i: ord(needle[i]) - ord("a")

        haystack_hash = needle_hash = 0

        for i in range(n):
            haystack_hash = (haystack_hash * a + h_to_int(i)) % modulus
            needle_hash = (needle_hash * a + needle_to_int(i)) % modulus
            if haystack_hash == needle_hash:
                return 0

        an = pow(a, n, modulus)

        for start in range(1, h - n + 1):
            haystack_hash = (
                haystack_hash * a - h_to_int(start - 1) * an + h_to_int(start + n - 1)
            ) % modulus
            if haystack_hash == needle_hash:
                return start

        return -1


# KMP
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # TODO
        pass
