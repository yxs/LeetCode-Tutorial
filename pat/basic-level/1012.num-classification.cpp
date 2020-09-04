#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

int main()
{
    int n, num, A1 = 0, A2 = 0, A5 = 0;
    double A4 = 0.0;
    cin >> n;
    vector<int> v[5];
    for (int i = 0; i != n; ++i)
    {
        cin >> num;
        v[num % 5].push_back(num);
    }
    for (int i = 0; i != 5; ++i)
    {
        for (int j = 0; j != v[i].size(); ++j)
        {
            // 偶数
            if (i == 0 && v[i][j] % 2 == 0)
                A1 += v[i][j];
            // 交错求和
            if (i == 1 && j % 2 == 0)
                A2 += v[i][j];
            if (i == 1 && j % 2 == 1)
                A2 -= v[i][j];
            // 余 3
            if (i == 3)
                A4 += v[i][j];
            // 余 4 且最大
            if (i == 4 && v[i][j] > A5)
                A5 = v[i][j];
        }
    }
    for (int i = 0; i != 5; ++i)
    {
        if (i != 0)
            cout << " ";
        if (i == 0 && A1 == 0 || i != 0 && v[i].size() == 0)
        {
            cout << "N";
            continue;
        }
        if (i == 0)
            cout << A1;
        if (i == 1)
            cout << A2;
        if (i == 2)
            cout << v[2].size();
        if (i == 3)
            cout << fixed << setprecision(1) << A4 / v[3].size();
        if (i == 4)
            cout << A5;
    }
    return 0;
}
