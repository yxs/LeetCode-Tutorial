from typing import List
from queue import Queue


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = [j for i in board for j in i]
        target = [1, 2, 3, 4, 5, 0]
        # 在一维字符串中，索引i在二维数组中的的相邻索引为neighbors[i]
        # 参考图
        # https://mmbiz.qpic.cn/sz_mmbiz_jpg/gibkIz0MVqdFSESAQTxkuSlldgYYM1Ipn48Xr4wvfQSYjUTqdeGsYw9pcX3Z5vzqAjMccSAsYXibqNbPuQlBvPBw/640?wx_fmt=jpeg
        neighbors = [[1, 3], [0, 4, 2], [1, 5], [0, 4], [3, 1, 5], [4, 2]]

        q = Queue()
        visited = list()
        q.put(start)
        visited.append(start)
        step = 0

        while not q.empty():
            sz = q.qsize()
            for i in range(sz):
                cur = q.get()
                # 达到目标布局
                if cur == target:
                    return step
                # 找到数字 0 的索引
                zero = cur.index(0)
                neighbor = neighbors[zero]
                # 将数字 0 和相邻的数字交换位置
                # adj = adjacency
                for idx, adj in enumerate(neighbor):
                    new_board = cur.copy()  # shallow copy
                    new_board[zero], new_board[adj] = new_board[adj], new_board[zero]
                    # 防止走回头路
                    if new_board not in visited:
                        visited.append(new_board)
                        q.put(new_board)
            step += 1

        return -1


board = [[1, 2, 3], [4, 0, 5]]

s = Solution()
print(s.slidingPuzzle(board))
