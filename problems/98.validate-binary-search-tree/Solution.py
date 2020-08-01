"""
@Date: 2020-05-05 10:01:22
@LastEditors: XueSong Ye
@LastEditTime: 2020-05-05 11:42:48
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float("-inf")
        while stack or root:
            # 从当前节点到左侧最深处的节点入栈
            while root:
                stack.append(root)
                root = root.left
            # 弹出栈顶
            root = stack.pop()

            # 当前节点应该大于所有左子树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True


s = Solution()

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print(s.isValidBST(root))
