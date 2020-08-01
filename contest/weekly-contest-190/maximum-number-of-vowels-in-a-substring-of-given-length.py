class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = ["a", "e", "i", "o", "u"]
        cnt = 0
        res = 0
        for i in range(k):  # 初始化滑动窗口
            if s[i] in v:
                cnt += 1
        res = cnt

        for b in range(len(s)):
            e = b + k
            if e >= len(s):
                break
            if s[e] in v:  # 右边界更新
                cnt += 1
            if s[b] in v:  # 左边界更新
                cnt -= 1
            res = max(res, cnt)
        return res


s = "weallloveyou"
k = 7
sol = Solution()
print(sol.maxVowels(s, k))
