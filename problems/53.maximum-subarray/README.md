[Solution](./Solution.cpp)

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

## 蛮力算法

The time complexity of this method is up to $`O(n^3)`$, run in cubic time.

两层遍历，枚举所有子区段，并对每个子区段求和，并取最大值。


## 蛮力算法的一点改进，递增策略

求和时复用之前的结果

## 分治

求得前缀、后缀的最大值

求得跨越前、后缀的最大值

## 贪心

从右向左迭代求和，小于 0 则重新计算。

## 动态规划

最大子区段取决于（之前的和加上当前值）与（当前值）中的较大者

https://www.zhihu.com/question/23995189/answer/613096905

## Ref links

https://leetcode-cn.com/problems/maximum-subarray/solution/zheng-li-yi-xia-kan-de-dong-de-da-an-by-lizhiqiang/

https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-cshi-xian-si-chong-jie-fa-bao-li-f/