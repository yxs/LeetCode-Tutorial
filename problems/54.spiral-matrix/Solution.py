from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        res = []
        start = 0
        rows, columns = len(matrix), len(matrix[0])

        while columns > start * 2 and rows > start * 2:
            x = columns - 1 - start
            y = rows - 1 - start
            # 左 -> 右
            for i in range(start, x + 1):
                res.append(matrix[start][i])
            # 上 -> 下
            if start < y:  # 终止行号大于起始行号，证明不止一行
                for i in range(start + 1, y + 1):
                    res.append(matrix[i][x])
            # 右 -> 左
            if start < x and start < y:  # 至少 2 行 2 列
                for i in range(x - 1, start - 1, -1):
                    res.append(matrix[y][i])

            # 下 -> 上
            if start < x and start < y - 1:  # 至少 3 行 2 列
                for i in range(y - 1, start, -1):
                    res.append(matrix[i][start])
            start += 1
        return res
