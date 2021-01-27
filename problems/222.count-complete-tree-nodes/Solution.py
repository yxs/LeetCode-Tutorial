import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# complete binary tree 必有一颗子树为 perfect binary tree
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        l = r = root
        h_l = h_r = 0
        while l != None:
            l = l.left
            h_l += 1
        while r != None:
            r = r.right
            h_r += 1
        if h_l == h_r:
            return int(math.pow(2, h_l) - 1)
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
