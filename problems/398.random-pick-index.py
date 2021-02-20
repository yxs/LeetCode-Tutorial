import random


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        reserve = None
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                count += 1
                rand = random.randint(1, count)
                if rand == count:
                    reserve = i
        return reserve


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
