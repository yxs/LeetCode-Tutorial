from typing import List


class Solution:
    class UnionFind:
        def __init__(self):
            self.parent = list(range(26))

        def find(self, index):
            if index == self.parent[index]:
                return index
            self.parent[index] = self.find(self.parent[index])  # 一直找父亲节点，直到根
            return self.parent[index]

        def union(self, index1, index2):
            self.parent[self.find(index1)] = self.find(index2)  # index1 根节点的父节点指向 index2 根节点

    def equationsPossible(self, equations: List[str]) -> bool:
        uf = Solution.UnionFind()
        for s in equations:
            if s[1] == "=":
                index1 = ord(s[0]) - ord("a")  # 转 ascii 后处理成数字
                index2 = ord(s[3]) - ord("a")
                uf.union(index1, index2)
        for s in equations:
            if s[1] == "!":
                index1 = ord(s[0]) - ord("a")
                index2 = ord(s[3]) - ord("a")
                if uf.find(index1) == uf.find(index2):
                    return False
        return True


equations = ["a==b","e==c","b==c","a!=e"]

sol = Solution()
print(sol.equationsPossible(equations))
