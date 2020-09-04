// https://pintia.cn/problem-sets/994805260223102976/problems/994805271455449088
#include <cstdio>
// 全排列中，每个数字都会在十位和各位分别出现 n-1 次
int main()
{
    int n, t, sum = 0;
    scanf("%d", &n);
    for (int i = 0; i != n; ++i)
    {
        scanf("%d", &t);
        sum += t * 10 * (n - 1) + t * (n - 1);
    }
    printf("%d", sum);
    return 0;
}
