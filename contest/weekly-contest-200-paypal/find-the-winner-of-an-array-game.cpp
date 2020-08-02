#include <vector>
#include <iostream>

using namespace std;

// 本解法超时了
class SolutionTLE
{
public:
    int getWinner(vector<int> &arr, int k)
    {
        if (k > arr.size())
        {
            auto it = max_element(begin(arr), end(arr));
            return *it;
        }

        int win = 0;
        while (k > win)
        {
            if (arr[0] > arr[1])
                ++win;
            else
            {
                swap(arr[0], arr[1]);
                win = 1;
            }

            // 记录并移除第一个元素
            int first = arr.front();
            arr.erase(arr.begin());

            // 循环左移
            int second = arr.front();
            arr.insert(arr.end(), second);
            arr.erase(arr.begin());

            // concatenate
            arr.insert(arr.begin(), first);
        }
        return arr[0];
    }
};

int main()
{
    vector<int> arr{2, 1, 3, 5, 4, 6, 7};
    int k = 2;
    SolutionTLE s;
    int res = s.getWinner(arr, k);
    cout << res;
    return 0;
}