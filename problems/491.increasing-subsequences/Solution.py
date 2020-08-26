from typing import List

# ?
class Solution1:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subs = {()}

        for num in nums:
            # ｜ 按位或运算符，取并集

            # sub + (num,)
            # tuple is immutable, add a number in this way.
            subs |= {sub + (num,) for sub in subs if not sub or sub[-1] <= num}

        return [sub for sub in subs if len(sub) >= 2]


# sol1 = Solution1()

# nums = [4, 6, 7, 7]
# print(sol1.findSubsequences(nums))


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []

        def dfs(cur, last, nums):
            if cur == len(nums):  # 枚举完
                if len(temp) >= 2:
                    ans.append(temp[:])
                return
            if nums[cur] >= last:  # 当前的元素大于等于上一个选择的元素
                temp.append(nums[cur])
                dfs(cur + 1, nums[cur], nums)
                temp.pop()
            if nums[cur] != last:
                dfs(cur + 1, last, nums)

        dfs(0, -float("inf"), nums)
        return ans


sol = Solution()

nums = [4, 6, 7, 7]
print(sol.findSubsequences(nums))
