# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                prev = succ = curr.left
                while prev.right:
                    prev = prev.right  # 当前节点的左子树的最右节点

                prev.right = curr.right
                curr.left = None
                curr.right = succ

            curr = curr.right
