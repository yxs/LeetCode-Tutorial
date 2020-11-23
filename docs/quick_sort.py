from typing import List
import random

# dj_khaled Solution
class Solutiondj_khaled:
    def quickSort(self, nums):
        def helper(head, tail):
            if head >= tail:
                return
            l, r = head, tail
            # 选取中间元素作为基准，不必最后再归位基准
            m = (r - l) // 2 + l
            pivot = nums[m]
            while r >= l:
                # 左向右，找大于基数的
                while r >= l and nums[l] < pivot:
                    l += 1
                # 右向左，找小于基数的
                while r >= l and nums[r] > pivot:
                    r -= 1
                # 找到，交换
                if r >= l:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
            helper(head, r)
            helper(l, tail)

        helper(0, len(nums) - 1)
        return nums


# CLRS Book Solution
class SolutionCLRS:
    def partition(self, nums: List[int], left: int, right: int):
        i = left - 1
        pivot = nums[right]  # pick last element as pivot
        # 区别于右左循环填坑法
        # 此方法通过两个指针，交换前i右移，j寻找小于基准的元素，换到左边
        for j in range(left, right):
            if nums[j] < pivot:
                i = i + 1
                nums[i], nums[j] = nums[j], nums[i]
        # 把基准放到正确位置
        nums[i + 1], nums[right] = nums[right], nums[i + 1]
        return i + 1

    def quick_sort(self, nums: List[int], left: int, right: int) -> List:
        if left < right:
            # pi is partitioning index
            pi = self.partition(nums, left, right)
            self.quick_sort(nums, left, pi - 1)
            self.quick_sort(nums, pi + 1, right)
        return nums


# quick sort should be in-place!
# The tradeoff in the code is it uses a bit of extra space
class SolutionTwohu:
    def quicksort(self, nums):
        if len(nums) <= 1:
            return nums

        pivot = random.choice(nums)
        lt = [v for v in nums if v < pivot]
        eq = [v for v in nums if v == pivot]
        gt = [v for v in nums if v > pivot]

        return self.quicksort(lt) + eq + self.quicksort(gt)


s1 = Solutiondj_khaled()
s2 = SolutionCLRS()
s3 = SolutionTwohu()  # shouldn't use

nums = [10, 7, 8, 9, 1, 5, 5]
n = len(nums)
print(s1.quickSort(nums))
print("------")
print(s2.quick_sort(nums, 0, n - 1))
print("------")
print(s3.quicksort(nums))

