from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(max(salary))
        salary.remove(min(salary))
        nums = len(salary)
        total_salary = sum(salary)
        ans = total_salary / nums
        return ans


salary = [4000, 3001, 1000, 2230, 2000]
sol = Solution()
print("%.5f" % sol.average(salary))
