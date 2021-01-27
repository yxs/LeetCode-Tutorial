from heapq import *


# 保证小顶堆large多一个元素
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # python heapq 是最小堆，pop返回的是最小项
        self.heaps = [], []

    def addNum(self, num: int) -> None:
        # small 大顶堆，保存小的一半
        # large 小顶堆，保存大的一半
        small, large = self.heaps
        # 1. 先往large里添加，然后再把large的堆顶元素（最小的）弹出
        # 2. 负号是对堆中的数字求反，添加到small中
        # 3. 如果large比small小，弹出small中最大的（heappop是弹出最小的，但是由于前面取反，所以，变成了弹出实际是最大的，也就是大顶堆的堆顶元素）
        # 4. 对弹出的元素取反，改回原来的值
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self) -> float:
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        # 之所以是 -，因为small里面的元素都是负的
        return (large[0] - small[0]) / 2.0


obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
obj.addNum(4)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
