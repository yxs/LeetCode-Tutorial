#include <iostream>

using namespace std;

int main()
{
    string a;
    int b, t = 0, tmp = 0;
    cin >> a >> b;
    int len = a.length();
    t = (a[0] - '0') / b;
    if ((t != 0 && len > 1) || len == 1)
        cout << t;
    tmp = (a[0] - '0') % b;
    for (int i = 1; i != len; ++i)
    {
        t = (tmp * 10 + a[i] - '0') / b;
        cout << t;
        tmp = (tmp * 10 + a[i] - '0') % b;
    }
    cout << " " << tmp;
    return 0;
}
