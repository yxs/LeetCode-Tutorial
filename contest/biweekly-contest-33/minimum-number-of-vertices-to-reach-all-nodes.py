from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        to = set(range(n))

        for edge in edges:
            if edge[1] in to:
                to.remove(edge[1])
        return list(to)


n = 6
edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]

sol = Solution()
print(sol.findSmallestSetOfVertices(n, edges))

