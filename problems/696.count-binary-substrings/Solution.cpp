#include <cstring>
#include <iostream>

using namespace std;

class Solution
{
public:
    int countBinarySubstrings(string s)
    {
        int cur = 1, pre = 0, res = 0;
        for (int i = 1; i < s.size(); ++i)
        {
            if (s[i] == s[i - 1])
                ++cur;
            else
            {
                res += min(cur, pre);
                pre = cur;
                cur = 1;
            }
        }
        return res + min(cur, pre);
    }
};

int main()
{
    string str = "00110011";
    Solution s;
    int res = s.countBinarySubstrings(str);
    cout << res;
    return 0;
}