// https://pintia.cn/problem-sets/994805260223102976/problems/994805277847568384
#include <iostream>

using namespace std;

int main()
{
    int n;
    scanf("%d", &n);
    int jia = 0, yi = 0, jiahan, jiahua, yihan, yihua, sum;
    for (int i = 0; i != n; ++i)
    {
        cin >> jiahan >> jiahua >> yihan >> yihua;
        sum = jiahan + yihan;
        if (sum == jiahua && sum != yihua)
            yi++;
        if (sum == yihua && sum != jiahua)
            jia++;
    }
    cout << jia << " " << yi;
    return 0;
}
