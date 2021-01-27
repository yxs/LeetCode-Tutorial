# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 反转以 head 为起点的 n 个节点，返回新的头结点
        def reverseN(head, n):
            if n == 1:
                # 记录第 n + 1 个节点
                successor = head.next
                return head, successor

            # 以 head.next 为起点，需要反转前 n - 1 个节点
            last, successor = reverseN(head.next, n - 1)
            head.next.next = head
            # 让反转之后的 head 节点和后面的节点连起来
            head.next = successor
            return last, successor

        if m == 1:
            res, _ = reverseN(head, n)
            return res
        # 前进到反转的起点触发 base case
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head
