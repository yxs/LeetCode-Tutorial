// https://pintia.cn/problem-sets/994805260223102976/problems/994805313708867584

#include <iostream>

using namespace std;

int main()
{
    int a, b, flag = 0;
    while (cin >> a >> b)
    {
        if (b != 0)
        {
            if (flag == 1)
                cout << " ";
            cout << a * b << " " << b - 1;
            flag = 1;
        }
    }
    // 没有输入或者仅一个常数的时候才输出 0 0，多项式末尾指数为 0 的是不输出的
    // 这个题意没怎么理解
    if (flag == 0)
        cout << "0 0";
    return 0;
}
