// https://pintia.cn/problem-sets/994805260223102976/problems/994805321640296448

// C 风格处理 IO 有点问题，为什么？
#include <iostream>

using namespace std;

int main()
{
    int n, score, min = 101, max = -1;
    string name, num, max_name, min_name, max_num, min_num;
    cin >> n;
    for (int i = 0; i != n; ++i)
    {
        cin >> name >> num >> score;
        if (score > max)
        {
            max = score;
            max_name = name;
            max_num = num;
        }
        if (score < min)
        {
            min = score;
            min_name = name;
            min_num = num;
        }
    }
    cout << max_name << " " << max_num << endl
         << min_name << " " << min_num;
    return 0;
}
