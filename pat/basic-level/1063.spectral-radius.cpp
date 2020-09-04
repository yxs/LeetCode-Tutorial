// https://pintia.cn/problem-sets/994805260223102976/problems/994805267860930560
#include <cmath>
#include <iomanip>
#include <iostream>

using namespace std;

int main()
{
    int n;
    float real, imaginary, ans, max = 0;
    cin >> n;
    for (int i = 0; i != n; ++i)
    {
        cin >> real >> imaginary;
        ans = sqrt(real * real + imaginary * imaginary);
        max = ans > max ? ans : max;
    }
    cout << setiosflags(ios::fixed);
    cout << setprecision(2) << max;
    return 0;
}
