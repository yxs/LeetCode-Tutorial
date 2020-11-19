## 如何理解动态规划？

*writes down "1+1+1+1+1+1+1+1 =" on a sheet of paper*

"What's that equal to?"

*counting* "Eight!"

*writes down another "1+" on the left*

"What about that?"

*quickly* "Nine!"

"How'd you know it was nine so fast?"

"You just added one more"

"So you didn't need to recount because you remembered there were eight! Dynamic Programming is just a fancy way to say 'remembering stuff to save time later'"

---

Introduction to Algorithms, 3rd Edition
 
When developing a dynamic-programming algorithm, we follow a sequence of four steps:
1. Characterize the structure of an optimal solution.
2. Recursively define the value of an optimal solution.
3. Compute the value of an optimal solution, typically in a bottom-up fashion.
4. Construct an optimal solution from computed information.

---

是否能使用 DP？

通过后无效性以及最优子结构判定

为什么 DP 高效？

自带剪枝，尽量缩小可能解空间

### 性质

1. 将一个问题拆成几个子问题，分别求解这些子问题，即可推断出大问题的解。
2. 无后效性：如果给定某一阶段的状态，则在这一阶段以后过程的发展不受这阶段以前各段状态的影响。
3. 最优子结构：大问题的最优解可以由小问题的最优解推出，这个性质叫做“最优子结构性质”。

### 思考路径：明确 base case -> 明确「状态」-> 明确「选择」 -> 定义 dp 数组/函数的含义

1. 暴⼒的递归解法 -> 带备忘录的递归解法 -> 迭代的动态规划解法
2. 找到状态和选择 -> 明确 dp 数组/函数的定义 -> 寻找状态之间的关系
3. 找出状态方程，数组压缩

![动态规划问题思考方向@liweiwei1419](https://pic.leetcode-cn.com/1f95da43d1bdeebdd1213bb804034ddc5f906dc61451cd63f2b5ab5d0eb33b33-%E3%80%8C%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E3%80%8D%E9%97%AE%E9%A2%98%E6%80%9D%E8%80%83%E6%96%B9%E5%90%91.png)

### 如何状态压缩

@labuladong 的讲解 https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/zhuang-tai-ya-suo-ji-qiao

最长回文子序列：

dp table 中，dp[i][j] 的状态只依赖于相邻的三个状态

左下，左，下

dp[i + 1][j - 1], dp[i][j - 1], dp[i + 1][j] 时

状态压缩，二维数组 dp table 变一维数组，去除 i，观察需要临时保存的那个值

动态规划技巧优化重叠子问题降低时间复杂度，最后尝试用状态压缩技巧优化空间复杂度



### KMP

移动位数 = 已匹配的字符数 - 对应的部分匹配值

"部分匹配值"就是"前缀"和"后缀"的最长的共有元素的长度


https://www.coursera.org/lecture/algorithms-part2/introduction-to-substring-search-n3ZpG

// TODO


## Most consistent ways of dealing with the series of stock problems

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems

https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/1.5-qi-ta-jing-dian-wen-ti/tuan-mie-gu-piao-wen-ti


第 i 天，
至今最多交易 k 次，
1 表示持有股票

dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])


## 打家劫舍系列


## References

1. [How should I explain dynamic programming to a 4-year-old?](https://www.quora.com/How-should-I-explain-dynamic-programming-to-a-4-year-old/answer/Jonathan-Paulson)
2. https://www.zhihu.com/question/23995189/answer/613096905
3. 算法小抄 @labuladong
4. https://zhuanlan.zhihu.com/p/91582909


