class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        # diagonals1 主对角线
        # diagonals2 次对角线
        def solve(row: int, columns: int, diagonals1: int, diagonals2: int):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                availablePositions = ((1 << n) - 1) & (
                    ~(columns | diagonals1 | diagonals2)
                )
                while availablePositions:
                    # 获得 x 的二进制表示中的最低位的 1 的位置
                    position = availablePositions & (-availablePositions)

                    # 将 x 的二进制表示中的最低位的 1 置成 0
                    availablePositions = availablePositions & (availablePositions - 1)

                    column = bin(position - 1).count("1")
                    queens[row] = column
                    solve(
                        row + 1,
                        columns | position,
                        (diagonals1 | position) << 1,
                        (diagonals2 | position) >> 1,
                    )

        solutions = list()
        queens = [-1] * n
        row = ["."] * n
        solve(0, 0, 0, 0)
        return solutions


sol = Solution()

print(sol.solveNQueens(4))
