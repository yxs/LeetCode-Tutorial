// https://pintia.cn/problem-sets/994805260223102976/problems/994805325918486528
#include <cstdio>

int main()
{
    int n, t = 0;
    scanf("%d", &n);
    while (n != 1)
    {
        n = n & 1 ? (3 * n + 1) / 2 : n / 2;
        ++t;
    }
    printf("%d", t);
    return 0;
}
