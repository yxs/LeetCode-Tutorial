二叉堆（Binary Heap）主要应用有两个，首先是一种排序方法「堆排序」，第二是一种「优先级队列」（Priority Queue）

二叉堆是存储在数组中的完全二叉树

```cpp
// 父节点的索引
int parent(int root) {
    return root / 2;
}
// 左孩子的索引
int left(int root) {
    return root * 2;
}
// 右孩子的索引
int right(int root) {
    return root * 2 + 1;
}
```