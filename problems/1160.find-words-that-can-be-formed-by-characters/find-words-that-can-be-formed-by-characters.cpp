// https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters/

#include <vector>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    int countCharacters(vector<string> &words, string chars)
    {
        if (words.size() == 0)
            return 0;
        unordered_map<char, int> chars_cnt;
        for (char c : chars)
            ++chars_cnt[c];
        int ans = 0;
        for (string word : words)
        {
            unordered_map<char, int> word_cnt;
            for (char c : word)
                ++word_cnt[c];
            bool is_ans = true;
            for (char c : word)
            {
                if (chars_cnt[c] < word_cnt[c])
                {
                    is_ans = false;
                    break;
                }
            }
            if (is_ans)
                ans += word.size();
        }
        return ans;
    }
};