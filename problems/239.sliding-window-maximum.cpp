#include <vector>
#include <deque>
#include <iostream>

using namespace std;

class Solution
{
public:
    // 维护单调递减的双端队列
    vector<int> maxSlidingWindow(vector<int> &nums, int k)
    {
        int n = nums.size();
        deque<int> q;
        // 单调递减的前k个的下标压入队列
        for (int i = 0; i < k; ++i)
        {
            while (!q.empty() && nums[i] >= nums[q.back()])
            {
                q.pop_back();
            }
            q.push_back(i);
        }
        // 第一个窗口状态的最大值显然是第一个
        vector<int> ans = {nums[q.front()]};
        for (int i = k; i < n; ++i)
        {
            while (!q.empty() && nums[i] >= nums[q.back()])
            {
                q.pop_back();
            }
            q.push_back(i);
            // 队首（元素下标）比当前窗口左侧小，说明当前队首不在窗口中了，弹出
            while (q.front() <= i - k)
            {
                q.pop_front();
            }
            ans.push_back(nums[q.front()]);
        }
        return ans;
    }
};

int main()
{
    vector<int> nums = {1, 3, -1, -3, 5, 3, 6, 7};
    int k = 3;
    Solution s;
    vector<int> res = s.maxSlidingWindow(nums, k);
    for (auto i : res)
        cout << i << ' ';
    // Output: [3,3,5,5,6,7]
    return 0;
}