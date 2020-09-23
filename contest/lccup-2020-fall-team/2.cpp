#include <vector>
#include <iostream>

using namespace std;

class Solution
{
public:
    bool isMagic(vector<int> target)
    {
        int n = target.size();
        vector<int> a;
        for (int i = 2; i <= n; i += 2)
        {
            a.push_back(i);
        }
        for (int i = 1; i <= n; i += 2)
        {
            a.push_back(i);
        }

        int k = n;
        for (int i = 0; i < n; ++i)
        {
            if (a[i] != target[i])
            {
                k = i;
                break;
            }
        }
        if (!k)
        {
            return false;
        }
        for (int i = 0; i < n; ++i)
        {
            a[i] = i + 1;
        }
        vector<int> answer;
        // for (auto i = a.begin(); i != a.end(); ++i)
        //     std::cout << *i << ' ';
        while (!a.empty())
        {
            vector<int> b;
            for (int i = 1; i < (int)a.size(); i += 2)
            {
                b.push_back(a[i]);
            }
            for (int i = 0; i < (int)a.size(); i += 2)
            {
                b.push_back(a[i]);
            }

            // for (auto i = b.begin(); i != b.end(); ++i)
            //     std::cout << *i << ' ';

            a.clear();
            for (int i = 0; i < (int)b.size(); ++i)
            {
                if (i < k)
                {
                    answer.push_back(b[i]);
                }
                else
                {
                    a.push_back(b[i]);
                }
            }
        }
        return target == answer;
    }
};


// Driver Code
int main()
{
    vector<int> target{2, 4, 3, 1, 5};
    Solution s;
    bool res = s.isMagic(target);
    cout << res;
    return 0;
}