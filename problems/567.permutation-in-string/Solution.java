import java.util.HashMap;

class Solution {
    // s2中是否包含s1全排列的任意一个
    public boolean checkInclusion(String s1, String s2) {
        if (s1 == null || s2 == null || s1.length() == 0 || s2.length() == 0 || s2.length() < s1.length())
            return false;

        // 目标子串
        HashMap<Character, Integer> need = new HashMap<Character, Integer>();
        // 窗口
        HashMap<Character, Integer> window = new HashMap<Character, Integer>();

        for (char c : s1.toCharArray())
            need.put(c, need.getOrDefault(c, 0) + 1); // {char: count, ...}

        int left = 0, right = 0;
        int valid = 0; // 已经匹配成功的字符种类数
        while (right < s2.length()) {
            // c 是将移入窗口的字符
            char c = s2.charAt(right);
            // 右移窗口
            right++;

            // 如果右指针现在滑到的字符是目标字符串的一个，那么更新窗口中的数据
            if (need.containsKey(c)) {
                window.put(c, window.getOrDefault(c, 0) + 1);
                if (window.get(c).equals(need.get(c))) // window char count == need char count
                    valid++;
            }
            /*** debug 输出的位置 ***/
            // System.out.printf("window: [%d, %d]\n", left, right);
            /********************/

            // 判断左侧窗口是否要收缩
            while (right - left >= s1.length()) {
                // 在这里判断是否找到了合法的子串
                if (valid == need.size())
                    return true;
                // 将移出窗口的字符
                char d = s2.charAt(left);
                left++;

                // 进行窗口内数据的一系列更新
                if (need.containsKey(d)) {
                    if (window.get(d).equals(need.get(d)))
                        valid--;
                    window.put(d, window.getOrDefault(d, 0) - 1);
                }
            }
        }
        return false;
    }
}