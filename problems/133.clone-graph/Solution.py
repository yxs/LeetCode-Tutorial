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

            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)

                visited[n].neighbors.append(visited[neighbor])

        return visited[node]
