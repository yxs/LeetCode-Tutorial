#include <vector>
#include <iostream>

using namespace std;

class Solution
{
public:
    // 从左往右填到第 first 个位置，当前排列为 output
    void backtrack(vector<vector<int>> &res, vector<int> &output, int first, int len)
    {
        // 所有数都填完了
        if (first == len)
        {
            res.emplace_back(output);
            return;
        }
        for (int i = first; i < len; ++i)
        {
            // 动态维护数组
            swap(output[i], output[first]);
            // 继续递归填下一个数
            backtrack(res, output, first + 1, len);
            // 撤销操作
            swap(output[i], output[first]);
        }
    }
    vector<vector<int>> permute(vector<int> &nums)
    {
        vector<vector<int>> res;
        // permute recursive
        backtrack(res, nums, 0, (int)nums.size());
        return res;
    }
};

int main()
{
    vector<int> nums = {1, 2, 3};
    Solution s;
    vector<vector<int>> ans = s.permute(nums);
    // Displaying the 2D vector
    for (int i = 0; i < ans.size(); i++)
    {
        for (int j = 0; j < ans[i].size(); j++)
            cout << ans[i][j] << " ";
        cout << endl;
    }
    return 0;
}