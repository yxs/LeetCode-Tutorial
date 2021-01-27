# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return None

        leftmost = root

        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                # 画图易得
                if head.next:  # 该节点和右侧节点属于同一个父节点，其右子节点和右侧节点的左子节点没有同一个父节点
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left

        return root
