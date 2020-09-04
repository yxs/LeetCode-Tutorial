#include <iostream>

using namespace std;

int main()
{
    int a, b, d;
    cin >> a >> b >> d;

    int t = a + b;
    if (t == 0)
    {
        cout << 0;
        return 0;
    }
    int s[100] = {0};
    int i = 0;
    while (t != 0)
    {
        // 取余，倒序输出即 d 进制，注意最后一次取余要舍弃掉
        s[i++] = t % d;
        t /= d;
    }
    for (int j = --i; j >= 0; --j)
        cout << s[j];
    return 0;
}
