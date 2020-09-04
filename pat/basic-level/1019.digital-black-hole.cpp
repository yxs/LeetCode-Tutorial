#include <bits/stdc++.h>

using namespace std;

int main()
{
    string s;
    cin >> s;
    s.insert(0, 4 - s.length(), '0');
    do
    {
        string a = s, b = s;
        sort(a.begin(), a.end(), greater<char>());
        sort(b.begin(), b.end());
        int res = stoi(a) - stoi(b);
        s = to_string(res);
        // 不足 4 位前面补 0
        s.insert(0, 4 - s.length(), '0');
        cout << a << " - " << b << " = " << s << endl;
    } while (s != "6174" && s != "0000");
    return 0;
}
