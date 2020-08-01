/*
 * @Date: 2020-05-04 18:47:43
 * @LastEditors: XueSong Ye
 * @LastEditTime: 2020-05-04 21:28:56
 */

#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> sortArrayByParity(vector<int> &A)
    {
        int l = 0;
        int r = A.size() - 1;
        while (l < r)
        {
            // even
            while (!(A[l] % 2) && l < r)
                ++l;
            // odd
            while (A[r] % 2 && l < r)
                --r;
            swap(A[l], A[r]);
        }
        return A;
    }
};

int main()
{
    vector<int> A{2, 2, 2, 2};
    vector<int> v;
    Solution s;
    v = s.sortArrayByParity(A);
    for (auto i : v)
        cout << i << " ";
    return 0;
}