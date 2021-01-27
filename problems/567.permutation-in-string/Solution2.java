// abstract all permutation strings of s to a map
// 全排列问题不需要考虑，原因是只需要考虑其元素和出现的频次，所以直接用s1就可以了
// 只有26个小写字母，所以可以用array代替map
// Q: s2中是否包含s1全排列的任意一个?
public class Solution2 {
    public boolean checkInclusion(String s1, String s2) {
        int len1 = s1.length(), len2 = s2.length();
        if (len1 > len2)
            return false;

        // Since there are only 26 lower case letters in this problem, we can just use
        // an array to represent the map.
        int[] count = new int[26];
        // sliding window


        // for (int i = 0; i < len1; i++) {
        //     count[s1.charAt(i) - 'a']++;
        //     count[s2.charAt(i) - 'a']--;
        // }
        // if (allZero(count))
        //     return true;

        // for (int i = len1; i < len2; i++) {
        //     count[s2.charAt(i) - 'a']--;
        //     count[s2.charAt(i - len1) - 'a']++;
        //     if (allZero(count))
        //         return true;
        // }


        // 记录目标字符和个数
        for (int i = 0; i < len1; i++) {
            count[s1.charAt(i) - 'a']++;
        }

        // 窗口维持len1大小
        for (int i = 0; i < len2; i++) {
            // 发现目标后， count-- 就会抵消掉之前的count++
            // When a character moves in from right of the window, we subtract 1 to that
            // character count from the map.
            count[s2.charAt(i) - 'a']--;
            // When a character moves out from left of the window, we add 1 to that
            // character count.
            // 非目标字符随着一进一出保持为0
            if (i - len1 >= 0)
                count[s2.charAt(i - len1) - 'a']++;
            if (allZero(count))
                return true;
        }

        return false;
    }

    private boolean allZero(int[] count) {
        for (int i = 0; i < 26; i++) {
            if (count[i] != 0)
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        String s = "ab";
        String t = "eidbaooo";
        Solution2 solution = new Solution2();
        boolean bool = solution.checkInclusion(s, t);
        System.out.println(bool);
    }
}
