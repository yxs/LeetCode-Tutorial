#include <string>
#include <vector>

using namespace std;

class Solution
{
public:
    string removeDuplicateLetters(string s)
    {
        vector<int> count(256, 0);
        vector<bool> visited(256, false);

        // 维护一个计数器记录字符串中字符的数量
        // 因为输入为 ASCII 字符，大小 256 够用了
        for (auto c : s)
            count[c]++;
        string result = "0";
        /** the key idea is to keep a monotically increasing sequence **/
        for (auto c : s)
        {
            // 每遍历过一个字符，都将对应的计数减一
            count[c]--;
            /** to filter the previously visited elements **/
            // 如果字符 c 存在栈中，直接跳过
            if (visited[c])
                continue;
            // 插入之前，和之前的元素比较一下大小
            // 如果字典序比前面的小，栈顶元素不是唯一的，pop 前面的元素
            while (c < result.back() && count[result.back()])
            {
                visited[result.back()] = false;
                result.pop_back();
            }
            result += c;
            visited[c] = true;
        }
        return result.substr(1);
    }
};