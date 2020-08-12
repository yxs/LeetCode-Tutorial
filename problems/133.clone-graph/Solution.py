from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        visited = {}

        queue = deque([node]) # 双端队列

        visited[node] = Node(node.val, [])

        while queue:
            n = queue.popleft()

            for neighboor in n.neighboors:
                if neighboor not in visited:
                    visited[neighboor] = Node(neighboor.val, [])
                    queue.append(neighboor)

                visited[n].neighboors.append(visited[neighboor])

        return visited[node]
