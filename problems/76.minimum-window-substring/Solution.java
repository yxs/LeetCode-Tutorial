import java.util.HashMap;

class Solution {
    public String minWindow(String s, String t) {
        // corner case
        if (s == null || t == null || s.length() == 0 || t.length() == 0 || s.length() < t.length())
            return "";

        // construct model
        int minLeft = 0;
        int minRight = 0;
        int min = s.length();
        boolean flag = false;

        HashMap<Character, Integer> map = new HashMap<Character, Integer>(); // {char: count, ...}

        int count = t.length(); // the number of characters that I need to match
        for (char c : t.toCharArray())
            map.put(c, map.getOrDefault(c, 0) + 1);

        int left = 0, right = 0;
        while (right < s.length()) {
            // c 是将移入窗口的字符
            char c = s.charAt(right);

            if (map.containsKey(c)) {
                map.put(c, map.get(c) - 1);
                if (map.get(c) >= 0) // 当且仅当已有字符串目标字符出现的次数小于目标字符串字符的出现次数时
                    count--; // if still unmatched characters, then count--
            }

            // if found a susbtring
            while (count == 0 && left <= right) {
                // update global min
                flag = true;
                int curLen = right + 1 - left;
                if (curLen <= min) {
                    minLeft = left;
                    minRight = right;
                    min = curLen;
                }

                // shrink left pointer
                char leftC = s.charAt(left);
                if (map.containsKey(leftC)) {
                    map.put(leftC, map.get(leftC) + 1);
                    // 如果左边即将要去掉的字符被目标字符串需要，且出现的频次正好等于指定频次，那么如果去掉了这个字符，
                    // 就不满足覆盖子串的条件，此时要破坏循环条件跳出循环，即控制目标字符串指定字符的出现总频次count++
                    if (map.get(leftC) >= 1)
                        count++;
                }
                left++;
            }
            right++;
        }
        return flag == true ? s.substring(minLeft, minRight + 1) : "";
    }

    public static void main(String[] args) {
        String s = "AADOBECODEBANC";
        String t = "ABC";
        Solution solution = new Solution();
        String window = solution.minWindow(s, t);
        System.out.println(window);
    }
}
