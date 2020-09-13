from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, _ in Counter(nums).most_common(k)]


# heap
# 哈希 + 小顶堆 / 手工建堆
class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def sift_down(arr, root, k):
            val = arr[root]
            while root << 1 < k:
                child = root << 1  # 左子节点
                if child | 1 < k and arr[child | 1][1] < arr[child][1]:
                    child |= 1  # 右子节点
                if arr[child][1] < val[1]:
                    arr[root] = arr[child]
                    root = child
                else:
                    break
            arr[root] = val

        def sift_up(arr, child):
            val = arr[child]
            while child >> 1 > 0 and val[1] < arr[child >> 1][1]:
                arr[child] = arr[child >> 1]
                child >>= 1
            arr[child] = val

        stat = Counter(nums)
        stat = list(stat.items())
        heap = [(0, 0)]

        # 构建规模为 k+1 的堆,新元素加入堆尾,上浮
        for i in range(k):
            heap.append(stat[i])
            sift_up(heap, len(heap) - 1)
        # 维护规模为 k+1 的堆,如果新元素大于堆顶,入堆,并下沉
        for i in range(k, len(stat)):
            if stat[i][1] > heap[1][1]:
                heap[1] = stat[i]
                sift_down(heap, 1, k + 1)
        return [item[0] for item in heap[1:]]


# quick sort
# TODO
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pass


nums = [1, 1, 1, 2, 2, 3]
k = 2
sol = Solution1()
print(sol.topKFrequent(nums, k))
