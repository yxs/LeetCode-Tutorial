#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

int main()
{
    string s = "AZXCVBDFGHC";
    // string s;
    // cin >> s;
    vector<char> v(s.begin(), s.end());
    unordered_map<char, int> dict;
    for (auto c : v)
    {
        if (++dict[c] == 2)
            cout << c;
    }
    return 0;
}