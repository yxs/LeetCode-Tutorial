class Solution {
    public int shipWithinDays(int[] weights, int D) {
        int left = 0, right = 0;
        for (int w : weights) {
            left = Math.max(left, w); // 最大值
            right += w; // 和
        }
        while (left < right) {
            int mid = left + (right - left) / 2, need = 1, cur = 0;
            for (int w : weights) {
                if (cur + w > mid) {
                    need += 1;
                    cur = 0;
                }
                cur += w;
            }
            if (need > D)
                left = mid + 1;
            else
                right = mid;
        }

        return left;
    }

    public static void main(String[] args) {
        int[] weights = {3,2,2,4,1,4};
        int D = 3;
        Solution solution = new Solution();
        int capacity = solution.shipWithinDays(weights, D);
        System.out.println(capacity);
    }
}