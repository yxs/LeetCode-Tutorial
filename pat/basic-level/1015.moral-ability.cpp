#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct node
{
    int num, moral, ability;
};

int cmp(struct node a, struct node b)
{
    if ((a.moral + a.ability) != (b.moral + b.ability))
        return (a.moral + a.ability) > (b.moral + b.ability);
    else if (a.moral != b.moral)
        return a.moral > b.moral;
    else
        return a.num < b.num;
}

int main()
{
    int n, low, high;
    scanf("%d %d %d", &n, &low, &high);
    vector<node> v[4];
    node tmp;
    int total = n;
    for (int i = 0; i < n; ++i)
    {
        scanf("%d %d %d", &tmp.num, &tmp.moral, &tmp.ability);
        if (tmp.moral < low || tmp.ability < low)
            total--;
        else if (tmp.moral >= high && tmp.ability >= high)
            v[0].push_back(tmp);
        else if (tmp.moral >= high && tmp.ability < high)
            v[1].push_back(tmp);
        else if (tmp.moral < high && tmp.ability < high && tmp.moral >= tmp.ability)
            v[2].push_back(tmp);
        else
            v[3].push_back(tmp);
    }
    printf("%d\n", total);
    for (int i = 0; i < 4; ++i)
    {
        sort(v[i].begin(), v[i].end(), cmp);
        for (int j = 0; j < v[i].size(); ++j)
            printf("%d %d %d\n", v[i][j].num, v[i][j].moral, v[i][j].ability);
    }
    return 0;
}
