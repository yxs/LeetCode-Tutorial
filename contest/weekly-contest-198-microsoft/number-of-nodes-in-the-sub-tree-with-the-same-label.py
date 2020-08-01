from collections import Counter
from collections import defaultdict
from typing import List

# ?
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(node: int, parent: int):
            cnt = Counter(labels[node])
            for child in g.get(node, []):
                if child != parent:
                    cnt += dfs(child, node)
            ans[node] = cnt[labels[node]]
            return cnt

        g, ans = defaultdict(list), [0] * n
        for a, b in edges:
            g[a] += [b]
            g[b] += [a]
        dfs(0, -1)
        return ans


n = 7
edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
labels = "aaabaaa"

sol = Solution()
print(sol.countSubTrees(n, edges, labels))

