// https://pintia.cn/problem-sets/994805260223102976/problems/994805267860930560
#include <cstdio>

const int N = 101;
int scores[N];
int ref_ans[N];

int main()
{
    int n, m, ans;
    scanf("%d%d", &n, &m);
    for (int i = 0; i != m; ++i)
    {
        scanf("%d", &scores[i]);
    }
    for (int i = 0; i != m; ++i)
    {
        scanf("%d", &ref_ans[i]);
    }
    for (int i = 0; i != n; ++i)
    {
        int total = 0;
        for (int j = 0; j != m; ++j)
        {
            scanf("%d", &ans);
            if (ans == ref_ans[j])
                total += scores[j];
        }
        printf("%d\n", total);
    }
    return 0;
}
