Reverse a singly linked list.

Example:
```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?


## 迭代

> 图源 https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/

注意：变量名不一致

![](https://pic.leetcode-cn.com/7d8712af4fbb870537607b1dd95d66c248eb178db4319919c32d9304ee85b602-%E8%BF%AD%E4%BB%A3.gif)

依次反转，显然时间复杂度为 $O(n)$，空间复杂度为 $O(1)$

1. 设置一个 prev 指向前面的哨兵，一个 curr 指向头节点
2. 暂存 curr 指向后一个节点的指针，否则在第 4 步就找不到后继了
3. curr 指向前一个节点
4. prev，curr 一起后移

## 递归

![](https://pic.leetcode-cn.com/dacd1bf55dec5c8b38d0904f26e472e2024fc8bee4ea46e3aa676f340ba1eb9d-%E9%80%92%E5%BD%92.gif)

$n_1 \rightarrow  \cdots  \rightarrow  n_{k-1} \rightarrow  n_k \rightarrow  n_{k+1} \leftarrow \cdots \leftarrow n_m$

假设一个中间状态，后半段已经反转，那么此时需要将当前节点的下一个节点的下一个指向当前节点

`head.next.next = head`

