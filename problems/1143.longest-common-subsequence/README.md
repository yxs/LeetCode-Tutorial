
Given two strings `text1` and `text2`, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

If there is no common subsequence, return 0.

 

Example 1:
```
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
```
Example 2:
```
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
```
Example 3:
```
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
```

Constraints:

- `1 <= text1.length <= 1000`
- `1 <= text2.length <= 1000`
- The input strings consist of lowercase English characters only.


[Solution](./Solution.cpp)

本问题可以参考算法导论，有详细介绍

### 暴力递归

$`O(2^n)`$

从右下角到左上，逐步剪去尾部的值

### 迭代

从递归颠倒过来，dp 状态转移方程

```
dp[i][j] = dp[i - 1][j - 1] + 1;

dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
```

此外，还可以通过状态压缩来降低空间复杂度
