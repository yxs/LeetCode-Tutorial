import collections


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 双向BFS，用集合记录两边的扩散，set效率比list高，便于判断是否发生交集
        start = {"0000"}
        end = {target}
        visited = set()  # 记录已经穷举过的密码，防止走回头路
        deadset = set(deadends)  # 记录需要跳过的死亡密码
        step = 0
        while start and end:
            # 每次都选择一个较小的集合进行扩散，那么占用的空间增长速度就会慢一些，效率就会高一些
            if len(start) > len(end):
                start, end = end, start
            temp = set()  # 记录扩散的结点
            for cur in start:  # 将 start 中的所有节点向周围扩散
                if cur in deadset:
                    continue
                if cur in end:  # 如果两边扩散的元素出现交集，说明找到了最短路径
                    return step
                visited.add(cur)
                # 将一个节点的未遍历相邻节点加入队列
                for i in range(4):  # 8 种可能
                    up = self.plusOne(cur, i)
                    if up not in visited:
                        temp.add(up)
                    down = self.minusOne(cur, i)
                    if down not in visited:
                        temp.add(down)
            step += 1
            # 交换start和end，end存储着上一次start扩散的结果temp
            start = end
            end = temp  # end始终记录上一次扩散时得到的元素
        return -1

    def plusOne(self, s: str, i: int) -> str:
        s_list = list(s)
        if s_list[i] == "9":
            s_list[i] = "0"
        else:
            s_list[i] = str(int(s_list[i]) + 1)
        return "".join(s_list)

    def minusOne(self, s: str, i: int) -> str:
        s_list = list(s)
        if s_list[i] == "0":
            s_list[i] = "9"
        else:
            s_list[i] = str(int(s_list[i]) - 1)
        return "".join(s_list)
