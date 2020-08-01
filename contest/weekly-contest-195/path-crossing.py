class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        s = set()
        s.add((x, y))  # 作为 tuple 放 set 中，后面用来查重
        d = {"N": (0, 1), "S": (0, -1), "W": (-1, 0), "E": (1, 0)}
        for i in range(len(path)):
            x += d[path[i]][0]
            y += d[path[i]][1]
            if (x, y) in s:
                return True
            s.add((x, y))
        return False


path = "NESWW"
sol = Solution()
print(sol.isPathCrossing(path))
