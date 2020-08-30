from collections import Counter


class Solution1:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for move in moves:
            if move == "U":
                y -= 1
            elif move == "D":
                y += 1
            elif move == "L":
                x -= 1
            elif move == "R":
                x += 1
        return x == y == 0


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = Counter(moves)
        return True if d["U"] == d["D"] and d["L"] == d["R"] else False


moves = "UD"
sol = Solution()
print(sol.judgeCircle(moves))
