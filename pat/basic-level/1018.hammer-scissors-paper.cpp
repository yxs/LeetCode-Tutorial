#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int jiawin = 0, yiwin = 0;
    // 0 锤子 C
    // 1 剪刀 J
    // 2 布 B
    int jia[3] = {0}, yi[3] = {0};
    // 相等时要按照字母顺序，写循环就应该考虑到
    for (int i = 0; i != n; ++i)
    {
        char s, t;
        cin >> s >> t;
        if (s == 'B' && t == 'C')
        {
            jiawin++;
            jia[0]++;
        }
        else if (s == 'B' && t == 'J')
        {
            yiwin++;
            yi[2]++;
        }
        else if (s == 'C' && t == 'B')
        {
            yiwin++;
            yi[0]++;
        }
        else if (s == 'C' && t == 'J')
        {
            jiawin++;
            jia[1]++;
        }
        else if (s == 'J' && t == 'B')
        {
            jiawin++;
            jia[2]++;
        }
        else if (s == 'J' && t == 'C')
        {
            yiwin++;
            yi[1]++;
        }
    }
    int ping = n - jiawin - yiwin;
    cout << jiawin << " " << ping << " " << yiwin << endl
         << yiwin << " " << ping << " " << jiawin << endl;
    int maxjia = jia[0] >= jia[1] ? 0 : 1;
    maxjia = jia[maxjia] >= jia[2] ? maxjia : 2;
    int maxyi = yi[0] >= yi[1] ? 0 : 1;
    maxyi = yi[maxyi] >= yi[2] ? maxyi : 2;
    char str[4] = {"BCJ"};
    cout << str[maxjia] << " " << str[maxyi];
    return 0;
}
