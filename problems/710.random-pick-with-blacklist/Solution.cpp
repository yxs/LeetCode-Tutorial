#include <vector>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    int sz;
    unordered_map<int, int> mapping;
    Solution(int N, vector<int> &blacklist)
    {
        // 取数据的部分
        sz = N - blacklist.size();
        for (int b : blacklist)
        {
            // 这里赋值多少都可以
            // 目的仅仅是把键存进哈希表
            // 方便快速判断数字是否在黑名单内
            mapping[b] = 666;
        }

        int last = N - 1;
        for (int b : blacklist)
        {
            // 如果 b 已经在区间 [sz, N)
            // 可以直接忽略
            if (b >= sz)
            {
                continue;
            }
            while (mapping.count(last))
            {
                last--;
            }
            mapping[b] = last;
            last--;
        }
    }

    int pick()
    {
        // 随机选取一个索引
        int index = rand() % sz;
        // 这个索引命中了黑名单，
        // 需要被映射到其他位置
        // 若没命中黑名单，则直接返回
        return mapping.count(index) ? mapping[index] : index;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(N, blacklist);
 * int param_1 = obj->pick();
 */