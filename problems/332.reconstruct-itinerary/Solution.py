import collections
import heapq
from typing import List

# 因为题目满足一笔画，因此最后一定是「死胡同」，也就是最后一个节点
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(curr: str):
            while vec[curr]:
                tmp = heapq.heappop(vec[curr])  # 取出最小元素
                dfs(tmp)
            stack.append(curr)

        vec = collections.defaultdict(list)
        for depart, arrive in tickets:
            vec[depart].append(arrive)
        # vec
        # defaultdict(<class 'list'>,
        # {'JFK': ['SFO', 'ATL'],
        #  'SFO': ['ATL'],
        #  'ATL': ['JFK', 'SFO']})
        for key in vec:
            heapq.heapify(vec[key])
            # vec 的 value 从 list 转换换 heap(堆，完全二叉树)，乱序的数组变成堆结构的数组
            # python 的 heapq 是最小堆，保证拆边顺序
            # {'JFK': ['ATL', 'SFO'],
            #  'SFO': ['ATL'],
            #  'ATL': ['JFK', 'SFO']}

        stack = list()
        dfs("JFK")
        return stack[::-1]  # 反向取值，步幅为1


tickets = [
    ["JFK", "SFO"],
    ["JFK", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "JFK"],
    ["ATL", "SFO"],
]

sol = Solution()
print(sol.findItinerary(tickets))
# ["JFK","ATL","JFK","SFO","ATL","SFO"]
