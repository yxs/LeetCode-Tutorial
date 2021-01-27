import java.util.HashMap;
import java.util.List;

// s 中找 p 的字母异位词（排列）子串
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        // 目标子串
        HashMap<Character, Integer> need = new HashMap<Character, Integer>();
        // 窗口
        HashMap<Character, Integer> window = new HashMap<Character, Integer>();

        for (char c : p.toCharArray())
            need.put(c, need.getOrDefault(c, 0) + 1); // {char: count, ...}

        int left = 0, right = 0;
        int valid = 0; // 已经匹配成功的字符种类数
        List<Integer> res = new ArrayList<>();

        while (right < s.length()) {
            char c = s.charAt(right);
            right++;

            if (need.containsKey(c)) {
                window.put(c, window.getOrDefault(c, 0) + 1);
                if (window.get(c).equals(need.get(c)))
                    valid++;
            }

            while (right - left >= p.length()) {
                if (valid == need.size())
                    res.add(left);
                char d = s.charAt(left);
                left++;

                if (need.containsKey(d)) {
                    if (window.get(d).equals(need.get(d)))
                        valid--;
                    window.put(d, window.getOrDefault(d, 0) - 1);
                }
            }

        }
        return res;
    }
}