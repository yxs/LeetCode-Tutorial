// https://pintia.cn/problem-sets/994805260223102976/problems/994805316250615808
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    vector<int> a(n);
    for (int i = 0; i != n; ++i)
    {
        cin >> a[i];
    }
    // m > n 时，其中 n 倍的数位移动是多余的
    m %= n;
    if (m != 0)
    {
        // 反转，不包括 last 元素
        reverse(begin(a), begin(a) + n);
        reverse(begin(a), begin(a) + m);
        reverse(begin(a) + m, begin(a) + n);
    }
    for (int i = 0; i != n - 1; ++i)
        cout << a[i] << " ";
    cout << a[n - 1];
    return 0;
}
