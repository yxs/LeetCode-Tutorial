# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        return self.build(nums, 0, n - 1)

    def build(self, nums: List[int], lo, hi):
        inf = int(1e9)
        if lo > hi:
            return None
        index = -1
        maxVal = -inf
        for i in range(lo, hi + 1):
            if maxVal < nums[i]:
                index = i
                maxVal = nums[i]

        root = TreeNode(maxVal)
        root.left = self.build(nums, lo, index - 1)
        root.right = self.build(nums, index + 1, hi)
        return root

