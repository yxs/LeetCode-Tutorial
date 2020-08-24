# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            leftH = height(root.left)
            rightH = height(root.right)
            if leftH == -1 or rightH == -1 or abs(leftH - rightH) > 1:
                return -1
            else:
                return max(leftH, rightH) + 1

        return height(root) >= 0
