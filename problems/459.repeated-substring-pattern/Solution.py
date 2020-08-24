
# https://leetcode-cn.com/problems/repeated-substring-pattern/solution/gou-zao-shuang-bei-zi-fu-chuan-by-elevenxx/
class Solution1:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)
        # return s in (s + s)[1:-1]

# KMP
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        pass