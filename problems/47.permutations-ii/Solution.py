# ?
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
            ans = [
                l[:i] + [n] + l[i:] for l in ans for i in range((l + [n]).index(n) + 1)
            ]
        return ans
