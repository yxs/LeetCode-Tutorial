import java.util.HashMap;

class Solution2 {
    public String minWindow(String s, String t) {
        // corner case
        if (s == null || t == null || s.length() == 0 || t.length() == 0 || s.length() < t.length())
            return "";

        // 目标子串
        HashMap<Character, Integer> need = new HashMap<Character, Integer>();
        // 窗口
        HashMap<Character, Integer> window = new HashMap<Character, Integer>();

        for (char c : t.toCharArray())
            need.put(c, need.getOrDefault(c, 0) + 1); // {char: count, ...}

        int left = 0, right = 0;
        int valid = 0; // 已经匹配成功的字符种类数

        int start = 0, len = Integer.MAX_VALUE;

        while (right < s.length()) {
            // c 是将移入窗口的字符
            char c = s.charAt(right);
            // 右移窗口
            right++;

            // 如果右指针现在滑到的字符是目标字符串的一个，那么更新窗口中的数据
            if (need.containsKey(c)) {
                window.put(c, window.getOrDefault(c, 0) + 1);
                if (window.get(c).equals(need.get(c))) // window char count == need char count
                    valid++;
            }

            // 判断左侧窗口是否要收缩
            while (valid == need.size()) {
                // 在这里更新最小覆盖子串
                if (right - left < len) {
                    start = left;
                    len = right - left;
                }
                // 将移出窗口的字符
                char d = s.charAt(left);
                left++;

                if (need.containsKey(d)) {
                    if (window.get(d).equals(need.get(d))) {
                        valid--;
                    }
                    window.put(d, window.getOrDefault(d, 0) - 1);
                }
            }
        }
        return len == Integer.MAX_VALUE ? "" : s.substring(start, start + len);
    }

    public static void main(String[] args) {
        String s = "AADOBECODEBANC";
        String t = "ABC";
        Solution2 solution = new Solution2();
        String window = solution.minWindow(s, t);
        System.out.println(window);
    }
}
