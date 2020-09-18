class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # 和最低位的 1 进行按位异或运算，就可以将其去除
        def flip(i: int, j: int, digit: int):
            row[i] ^= (1 << digit)
            column[j] ^= (1 << digit)
            sub_box[i // 3][j // 3] ^= (1 << digit)

        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return

            i, j = spaces[pos]
            # 按位或，按位取翻，再按位与，讲无关位置为 0，变成第 k 位为 1，表示该位置可以填入数字 k+1
            mask = ~(row[i] | column[j] | sub_box[i // 3][j // 3]) & 0x1ff  # 111111111


            # for digit in range(9):
            #     if row[i][digit] == column[j][digit] == sub_box[i // 3][j // 3][digit] == False:
            #         row[i][digit] = column[j][digit] = sub_box[i // 3][j // 3][digit] = True
            #         board[i][j] = str(digit + 1)
            #         dfs(pos + 1)
            #         row[i][digit] = column[j][digit] = sub_box[i // 3][j // 3][digit] = False
            #     if valid:
            #         return

            while mask:
                digitMask = mask & (-mask)  # 得到二进制表示中最低位的 1
                digit = bin(digitMask).count("0") - 1
                flip(i, j, digit)
                board[i][j] = str(digit + 1)
                dfs(pos + 1)
                flip(i, j, digit)
                mask &= (mask - 1)
                if valid:
                    return

        # row = [[False] * 9 for _ in range(9)]
        # column = [[False] * 9 for _ in range(9)]
        # sub_box = [[[False] * 9 for _a in range(3)] for _b in range(3)]

        row = [0] * 9
        column = [0] * 9
        sub_box = [[0] * 3 for _ in range(3)]
        valid = False
        spaces = list()

        # 初始化，已有数字改为 True

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    digit = int(board[i][j]) - 1
                    flip(i, j, digit)
        
        while True:
            modified = False
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        mask = ~(row[i] | column[j] | sub_box[i // 3][j // 3]) & 0x1ff
                        if not (mask & (mask - 1)):  # 按位与运算后得到 0，该空白格只有唯一的数可以填入
                            digit = bin(mask).count("0") - 1  # 1~9 用 0～8 来存储
                            flip(i, j, digit)
                            board[i][j] = str(digit + 1)
                            modified = True
            if not modified:
                break

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i, j))
                # else:
                    # digit = int(board[i][j]) - 1  # row[2][3]=True 表示数字 4 在第 2 行已经出现过
                    # row[i][digit] = column[j][digit] = sub_box[i // 3][j // 3][digit] = True
                    

        dfs(0)
