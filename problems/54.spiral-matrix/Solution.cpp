#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> spiralOrder(vector<vector<int>> &matrix)
    {
        if (matrix.empty())
            return {};
        vector<int> res = {};
        int start = 0;
        int rows = matrix.size();
        int columns = matrix[0].size();

        // 此边界条件优于每个边界去检测
        while (columns > start * 2 && rows > start * 2)
        {
            int endX = columns - 1 - start;
            int endY = rows - 1 - start;

            // from left to right
            for (int i = start; i <= endX; ++i)
                res.push_back(matrix[start][i]);

            // from top to bottom
            if (start < endY)
            {
                for (int i = start + 1; i <= endY; ++i)
                    res.push_back(matrix[i][endX]);
            }

            // from right to left
            if (start < endX && start < endY)
            {
                for (int i = endX - 1; i >= start; --i)
                    res.push_back(matrix[endY][i]);
            }

            // from bottom to top
            if (start < endX && start < endY - 1)
            {
                for (int i = endY - 1; i >= start + 1; --i)
                    res.push_back(matrix[i][start]);
            }
            ++start;
        }
        return res;
    }
};

// Driver Code
int main()
{
    vector<vector<int>> matrix{{1, 2, 3, 4},
                               {5, 6, 7, 8},
                               {9, 10, 11, 12}};
    Solution s;
    auto res = s.spiralOrder(matrix);
    for (auto i : res)
        cout << i << " ";
    return 0;
}