class Solution:
    def maxSubArray(self, nums) -> int:
        max_so_far = nums[0]  # 全局最大
        max_ending_here = nums[0]  # 最大子区段，取决于（之前的和加上当前值）与（当前值）中的较大者
        for i in range(1, len(nums)):
            max_ending_here = max(nums[i], max_ending_here + nums[i])
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

s = Solution()
print(s.maxSubArray(nums))
