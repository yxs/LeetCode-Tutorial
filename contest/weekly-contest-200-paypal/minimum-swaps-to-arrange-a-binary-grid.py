class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        suffix = []  # 每一行为 0 的后缀个数s
        for i in range(n):
            j = n - 1
            while j >= 0 and grid[i][j] == 0:
                j -= 1
            suffix.append(n - 1 - j)

        cnt = 0
        for i in range(n - 1):
            valid = n - 1 - i

            j = i
            while j < len(suffix) and suffix[j] < valid:
                j += 1

            if j == len(suffix):
                return -1

            cnt += j - i

            while j > i:
                suffix[j], suffix[j - 1] = suffix[j - 1], suffix[j]
                j -= 1
        return cnt
