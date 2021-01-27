class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, res = [], [-1] * len(nums)
        # 将数组长度翻倍，解决循环问题
        for i in range(len(nums)) * 2:
            # stack 不为空且栈顶元素小于当前元素，意味着当前元素比它后面的元素高
            while stack and (nums[stack[-1]] < nums[i]):
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res