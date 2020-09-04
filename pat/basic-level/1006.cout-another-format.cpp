// https://pintia.cn/problem-sets/994805260223102976/problems/994805318855278592
#include <iostream>

using namespace std;

int main()
{
    int n, i = 0;
    int a[3] = {0};
    cin >> n;
    while (n != 0)
    {
        a[i++] = n % 10;
        n = n / 10;
    }
    for (int i = 0; i < a[2]; i++)
        cout << "B";
    for (int i = 0; i < a[1]; i++)
        cout << "S";
    for (int i = 0; i < a[0]; i++)
        cout << i + 1;
    return 0;
}
