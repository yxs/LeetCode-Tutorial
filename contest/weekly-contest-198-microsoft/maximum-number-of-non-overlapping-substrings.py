from typing import List

# interval scheduling maximization problem (ISMP) (https://en.wikipedia.org/wiki/Interval_scheduling)
class Solution:
    def maxNumOfSubstrings(self, s):
        fst = {c: s.index(c) for c in set(s)}  # k, v 结构左边界
        lst = {c: s.rindex(c) for c in set(s)}  # 右边界
        intervals = []
        for c in set(s):
            b, e = fst[c], lst[c]
            i = b
            # 扩展区间，目标字符 a 区间中包含的字符 b 的区间也要考虑
            while i <= e:
                b = min(b, fst[s[i]])
                e = max(e, lst[s[i]])
                i += 1
            if b == fst[c]:  # 避免向左扩展「该条件换成向右也行」时发生重复，本例 s 中，d 会和 a 重复
                intervals.append((e, b))  # 便于通过结尾位置排序

        intervals.sort()
        ans, prev = [], -1
        for e, b in intervals:
            if b > prev:
                ans.append(s[b : e + 1])
                prev = e

        return ans


sol = Solution()
s = "adefaddaccc"
print(sol.maxNumOfSubstrings(s))
