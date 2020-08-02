from typing import List

# CPP 也超时 https://leetcode-cn.com/submissions/detail/93845639/testcase/
class SolutionTLE:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k > len(arr):
            return max(arr)
        win = 0
        while k > win:
            if arr[0] > arr[1]:
                win += 1
            else:
                arr[0], arr[1] = arr[1], arr[0]
                win = 1

            subarr = arr[1:]
            arr = arr[:1] + subarr[1:] + subarr[:1]

        return arr[0]


# 不必交换元素
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k > len(arr):
            return max(arr)
        cur = arr[0]
        win = 0
        for i in range(1, len(arr)):
            if arr[i] > cur:
                cur = arr[i]
                win = 0
            win += 1
            if win == k:
                break
        return cur


# arr = [2, 1, 3, 5, 4, 6, 7]
# k = 2

# arr = [3, 2, 1]
# k = 10

arr = [1, 11, 22, 33, 44, 55, 66, 77, 88, 99]
k = 1000000000
sol = Solution()
print(sol.getWinner(arr, k))
