class Solution {
    public int minEatingSpeed(int[] piles, int H) {
        int lo = 1;
        int hi = 1_000_000_000; // _ 提升可读性

        while (lo < hi) {
            int mi = (lo + hi) / 2;
            if (!possible(piles, H, mi))
                lo = mi + 1;
            else
                hi = mi;

        }
        return lo;
    }

    public boolean possible(int[] piles, int H, int K) {
        int time = 0;
        for (int p : piles)
            time += (p - 1) / K + 1; // Math.ceil(p / K) 向上取整
        return time <= H;
    }

    public static void main(String[] args) {
        int[] piles = { 3, 6, 7, 11 };
        int H = 8;
        Solution solution = new Solution();
        int speed = solution.minEatingSpeed(piles, H);
        System.out.println(speed);
    }
}