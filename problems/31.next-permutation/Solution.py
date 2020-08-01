class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:  # 从右向左遍历预期为递减的子序列，找到第一个不满足的元素 k
            i -= 1
        if i == 0:  # 整个序列为递减
            nums.reverse()
            return
        k = i - 1
        while nums[j] <= nums[k]:  # 从右向左找到一个小于 k 的元素并交换
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        l, r = k + 1, len(nums) - 1
        while l < r:  # 反转 k 之后的元素
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
