// https://pintia.cn/problem-sets/994805260223102976/problems/994805317546655744
// 判断到根号下 x 即可

#include <iostream>

using namespace std;

bool isprime(int a)
{
    for (int i = 2; i * i <= a; ++i)
        if (a % i == 0)
            return false;
    return true;
}

int main()
{
    int n, t = 0;
    cin >> n;
    for (int i = 5; i <= n; ++i)
        if (isprime(i - 2) && isprime(i))
            t++;
    cout << t;
    return 0;
}
