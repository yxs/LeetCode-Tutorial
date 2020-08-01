#include <algorithm>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<string> topKFrequent(vector<string> &words, int k)
    {
        unordered_map<string, int> dict;
        for (const string &s : words) // 生成字典，key 为单词，value 为个数。{"leetcode": 1, ...}
            dict[s]++;

        priority_queue<pair<string, int>, vector<pair<string, int>>, Comp> pq;

        // {"i": 2, "love": 2, "coding": 1, "leetcode": 1}
        for (const auto &pa : dict)
        {
            pq.push(pa);
            if (pq.size() > k)
                // 移除队首元素，即堆顶元素，也是 smallest element
                pq.pop();
        }
        vector<string> result;
        // 此时 pq 中只有 {"i": 2, "love": 2}
        while (!pq.empty())
        {
            result.push_back(pq.top().first);
            pq.pop();
        }
        // 由于上面依次是从队首去元素，然后 push 到 vector 中，因此需要将 love, i 反转成 i, love
        reverse(result.begin(), result.end());
        return result;
    }

private:
    struct Comp
    {
        Comp() {}
        ~Comp() {}
        bool operator()(const pair<string, int> &a, const pair<string, int> &b)
        {
            // 构造最小堆，降序排列；出现单词次数一样时，构造最小堆，升序排列
            return a.second > b.second || (a.second == b.second && a.first < b.first);
        }
    };
};

// 测试样例
int main()
{
    vector<string> words{"i", "love", "leetcode", "i", "love", "coding"};
    int k = 2;
    Solution solution;
    auto res = solution.topKFrequent(words, k);
    for (auto i = res.begin(); i != res.end(); ++i)
    {
        cout << *i << ' ';
    }
    return 0;
}