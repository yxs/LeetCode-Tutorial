#include <bits/stdc++.h>

using namespace std;

struct mooncake
{
    float mount, price, unit;
};

int cmp(mooncake a, mooncake b)
{
    return a.unit > b.unit;
}

int main()
{
    int n, d;
    cin >> n >> d;
    vector<mooncake> a(n);
    for (int i = 0; i != n; ++i)
        scanf("%f", &a[i].mount);
    for (int i = 0; i != n; ++i)
        scanf("%f", &a[i].price);
    for (int i = 0; i != n; ++i)
        a[i].unit = a[i].price / a[i].mount;
    sort(a.begin(), a.end(), cmp); // greater<mooncake>() 不能用的原因？
    float res = 0.0;
    for (int i = 0; i < n; ++i)
    {
        if (a[i].mount <= d)
        {
            res = res + a[i].price;
        }
        else
        {
            res = res + a[i].unit * d;
            break;
        }
        d = d - a[i].mount;
    }
    printf("%.2f", res);
    return 0;
}
