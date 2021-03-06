class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        n, m = len(board), len(board[0])  # rows, columns

        def dfs(x, y):
            if not 0 <= x < n or not 0 <= y < m or board[x][y] != "O":
                return

            board[x][y] = "#"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        # 左右边查找O以及与O相连的O，改为#
        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)
        # 上下
        for i in range(m - 1):
            dfs(0, i)
            dfs(n - 1, i)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

