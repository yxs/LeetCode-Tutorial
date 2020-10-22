#include <string>
#include <iostream>

using namespace std;

class Solution
{
    int s[100005];

public:
    int minimumOperations(string leaves)
    {
        int n = leaves.size(), i, j, ans = n;
        for (i = 0; i < n; i++)
            s[i + 1] = s[i] + (leaves[i] == 'y');
        for (i = 1; i < n; i++)
            s[i] = i - 2 * s[i];
        for (i = 2, j = s[1]; i < n; i++)
        {
            ans = min(ans, s[n] + s[i] - j);
            j = max(j, s[i]);
        }
        return ans;
    }
};

int main()
{
    string s = "rrryyyrryyyrr";
    Solution sol;
    int res = sol.minimumOperations(s);
    cout << res;
}