// https://pintia.cn/problem-sets/994805260223102976/problems/994805323154440192
// 只能有一个 P 一个 T，中间末尾和开头可以随便插入 A
// 但是必须满足开头的 A 的个数 * 中间的 A 的个数 = 结尾的 A 的个数，而且 P 和 T 中间不能没有 A
#include <iostream>
#include <map>

using namespace std;

int main()
{
    int n, p = 0, t = 0;
    string s;
    cin >> n;
    for (int i = 0; i != n; ++i)
    {
        cin >> s;
        map<char, int> m;
        for (int j = 0; j != s.size(); ++j)
        {
            m[s[j]]++;
            if (s[j] == 'P')
                p = j;
            if (s[j] == 'T')
                t = j;
        }
        if (m['P'] == 1 && m['A'] != 0 && m['T'] == 1 && m.size() == 3 && t - p != 1 && p * (t - p - 1) == s.length() - t - 1)
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}
