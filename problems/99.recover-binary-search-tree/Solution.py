# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Morris (InOrder) traversal ?
# 建立一种机制，对于没有左子树的节点只到达一次，对于有左子树的节点会到达两次
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        x, y, pred = None, None, None
        while root:
            if root.left:
                # 左一步，一直向右找到左子树上最右的节点 predecessor
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right

                # predecessor 的右指针指向 root
                if not predecessor.right:
                    predecessor.right = root
                    root = predecessor.left
                    continue
                predecessor.right = None  # 左子树已经访问完了，断开链接

            if pred and pred.val > root.val:
                if not x:
                    x = pred
                y = root
            pred = root
            root = root.right
        x.val, y.val = y.val, x.val
