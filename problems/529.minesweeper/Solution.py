class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        direction = (
            (0, 1),  # 上
            (1, 0),  # 右
            (0, -1),  # 下
            (-1, 0),  # 左
            (1, 1),  # 右上
            (1, -1),  # 右下
            (-1, 1),  # 左上
            (-1, -1),  # 左下
        )
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"  # 规则 1，游戏就结束
            return board

        self.m, self.n = len(board), len(board[0])

        def check(i, j):
            cnt = 0
            for x, y in direction:
                x, y = x + i, y + j
                if 0 <= x < self.m and 0 <= y < self.n and board[x][y] == "M":
                    cnt += 1
            return cnt  # 周围相邻的方块里地雷的数量，规则 3

        def dfs(i, j):
            cnt = check(i, j)
            if not cnt:
                board[i][j] = "B"  # 规则 2，没有相邻地雷的空方块被挖出
                for x, y in direction:
                    x, y = x + i, y + j
                    if 0 <= x < self.m and 0 <= y < self.n and board[x][y] == "E":
                        dfs(x, y)
            else:
                board[i][j] = str(cnt)

        dfs(click[0], click[1])
        return board

