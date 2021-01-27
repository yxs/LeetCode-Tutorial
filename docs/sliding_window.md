https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem





@labuladong写的C++

```cpp
/* 滑动窗口算法框架 */
void slidingWindow(string s, string t) {
    unordered_map<char, int> need, window;
    for (char c : t) need[c]++;

    int left = 0, right = 0;
    int valid = 0; // 窗口中满足need条件的字符个数(种类数)
    while (right < s.size()) {
        // c 是将移入窗口的字符
        char c = s[right];
        // 右移窗口
        right++;
        // 进行窗口内数据的一系列更新
        ...

        /*** debug 输出的位置 ***/
        printf("window: [%d, %d)\n", left, right);
        /********************/

        // 判断左侧窗口是否要收缩
        while (window needs shrink) {
            // d 是将移出窗口的字符
            char d = s[left];
            // 左移窗口
            left++;
            // 进行窗口内数据的一系列更新
            ...
        }
    }
}
```

Java
```java
// source string 中查找 target string
public void slidingWindow(String s, String t) {
    // corner case
    if (s == null || t == null || s.length() == 0 || t.length() == 0 || s.length() < t.length())
        return "";

    HashMap<Character, Integer> need = new HashMap<Character, Integer>(); // 目标子串
    HashMap<Character, Integer> window = new HashMap<Character, Integer>(); // 窗口

    for (char c : t.toCharArray())
        need.put(c, need.getOrDefault(c, 0) + 1); // {char: count, ...}

    int left = 0, right = 0;
    int valid = 0; // 已经匹配成功的字符种类数
    while (right < s.length()) {
        // c 是将移入窗口的字符
        char c = s.charAt(right);
        // 右移窗口
        right++;

        // 如果右指针现在滑到的字符是目标字符串的一个，那么更新窗口中的数据
        ...

        /*** debug 输出的位置 ***/
        System.out.println("window: [%d, %d)\n", left, right);
        /********************/

        // 判断左侧窗口是否要收缩
        while (window needs shrink) {
            // 将移出窗口的字符
            char d = s.charAt(left);
            left++;

            // 进行窗口内数据的一系列更新
            ...
        }
    }
}
```

以 leetcode 76 minimum-window-substring

source string 中查找是否存在包含target string 的「窗口」

来看，向右滑动/从左边缩小时，更新 window(char: count) 哈希表，通过vaild变量去判定need string是否被匹配到了，在缩小窗口前，记录当前的窗口大小
