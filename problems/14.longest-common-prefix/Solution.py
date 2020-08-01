class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        m, M = min(strs), max(strs)  # 字典序最小和最大的字符串比较即可
        for i in range(len(m)):
            if m[i] != M[i]:
                return m[:i]
        return m


sol = Solution()
print(sol.longestCommonPrefix())
