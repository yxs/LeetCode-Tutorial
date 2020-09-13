from typing import List
from collections import Counter


class Solution1:
    def numSpecial(self, mat: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i: int, j: int):
            for di, dj in directions:
                newi, newj = i + di, j + dj
                while 0 <= newi < len(mat) and 0 <= newj < len(mat[0]):
                    if mat[newi][newj] != 0:
                        return 0
                    newi += di
                    newj += dj
            return 1

        h, w = len(mat), len(mat[0])
        cnt = 0
        for i in range(h):
            for j in range(w):
                if mat[i][j] == 1:
                    cnt += check(i, j)
                    break
        return cnt


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        h, w = len(mat), len(mat[0])  # 高，宽
        counter_x = [Counter(mat[i]) for i in range(h)]  # 每行 0 1 个数
        counter_y = [Counter([n[i] for n in mat]) for i in range(w)]  # 每列 0 1 个数
        ans = 0
        for i in range(h):
            for j in range(w):
                # 该行，该列只有一个
                if mat[i][j] == 1 and counter_x[i][1] == 1 and counter_y[j][1] == 1:
                    ans += 1
        return ans


mat1 = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]

mat2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

mat3 = [[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]

mat4 = [
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
]

sol = Solution()
print(sol.numSpecial(mat4))
