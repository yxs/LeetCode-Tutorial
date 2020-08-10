class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # [2, 2, 2, 2] 分段 0, 1 数量
        s = [len(i) for i in s.replace("01", "0 1").replace("10", "1 0").split()]

        # map the similar index of multiple containers
        return sum(min(a, b) for a, b in zip(s, s[1:]))


s = "00110011"
sol = Solution()
print(sol.countBinarySubstrings(s))