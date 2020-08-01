/*
 * @Author: xuesong.ye 
 * @Date: 2020-04-22 21:34:11 
 * @Last Modified by: xuesong.ye
 * @Last Modified time: 2020-04-22 21:38:55
 */

// 面试题04. 二维数组中的查找
// 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

// 示例:

// 现有矩阵 matrix 如下：

// [
//   [1,   4,  7, 11, 15],
//   [2,   5,  8, 12, 19],
//   [3,   6,  9, 16, 22],
//   [10, 13, 14, 17, 24],
//   [18, 21, 23, 26, 30]
// ]

// 给定 target = 5，返回 true。
// 给定 target = 20，返回 false。

// 限制：

// 0 <= n <= 1000
// 0 <= m <= 1000

// 注意：本题与主站 240 题相同：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/

// ============解题思路============

// 从右上角 i 开始查找，若目标 e < i，则该列均大于 e，移除该列
// 若 e > i，则改行均小于 e，移除该行
// 一直保持 i 位于右上角

// https://github.com/yxs/CodingInterviewChinese2/blob/master/04_FindInPartiallySortedMatrix/FindInPartiallySortedMatrix.cpp

#include <iostream>
#include <vector>

using namespace std;

// ============ 观察规律，单调路径算法：O(m + n) 时间复杂度，O(1) 空间复杂度 ============
class Solution
{
public:
    bool findNumberIn2DArray(vector<vector<int>> &matrix, int target)
    {
        bool found = false;
        if (!matrix.empty())
        {
            int rows = matrix.size();
            int columns = matrix[0].size();
            int row = 0;
            int column = columns - 1;
            while (row < rows && column >= 0)
            {
                if (matrix[row][column] == target)
                {
                    found = true;
                    break;
                }
                else if (matrix[row][column] > target)
                    --column;
                else
                    ++row;
            }
        }
        return found;
    }
};

// Driver Code
int main()
{
    vector<vector<int>> vec{{1, 4, 7, 11, 15},
                            {2, 5, 8, 12, 19},
                            {3, 6, 9, 16, 22},
                            {10, 13, 14, 17, 24},
                            {18, 21, 23, 26, 30}};
    Solution s;
    bool res = s.findNumberIn2DArray(vec, 5);
    cout << boolalpha;
    cout << res;
    return 0;
}