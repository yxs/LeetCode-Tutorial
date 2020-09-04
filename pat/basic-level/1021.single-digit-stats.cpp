#include <bits/stdc++.h>

using namespace std;

int main()
{
    string s;
    cin >> s;
    int m[10] = {0};
    for (unsigned int i = 0; i != s.length(); ++i)
        m[s[i] - '0']++;
    for (int i = 0; i != 10; ++i)
    {
        if (m[i] != 0)
            printf("%d:%d\n", i, m[i]);
    }
    return 0;
}
