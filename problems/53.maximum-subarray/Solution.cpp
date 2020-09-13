#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

// brute force solution.
// The time complexity of this method is up to O(n^3), run in cubic time.
// 两层遍历，枚举所有子区段，并对每个子区段求和，并取最大值。
class SolutionBF
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int size = nums.size();
        int gs = nums[0];
        for (int i = 0; i < size; ++i)
        {
            for (int j = 0; j < size; ++j) // Enumerate all sections
            {
                int s = 0;
                for (int k = i; k <= j; ++k)
                    s += nums[k];
                if (gs < s)
                    gs = s;
            }
        }
        return gs;
    }
};

// incremental strategy, a little improvement, but not enough. O(n^2)
// 递增策略，求和时复用之前的结果
class SolutionIC
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int size = nums.size();
        int gs = nums[0];
        for (int i = 0; i < size; ++i)
        {
            int s = 0;
            for (int j = i; j < size; ++j)
            {
                // Add a node to the calculation of the sub-section to avoid repeated calculations.
                s += nums[j];
                if (gs < s)
                    gs = s;
            }
        }
        return gs;
    }
};

// divide and conquer. O(nlogn)
// 求得前缀、后缀的最大值
// 求得跨越前、后缀的最大值
class SolutionDC
{
public:
    int gs_DC(vector<int> &nums, int lo, int hi)
    {
        if (hi - lo < 2)
            return nums[lo];
        int mi = (lo + hi) / 2;
        int gsL = nums[mi - 1], sL = 0, i = mi;
        while (lo < i--)
            if (gsL < (sL += nums[i]))
                gsL = sL;
        int gsR = nums[mi], sR = 0, j = mi - 1;
        while (++j < hi)
            if (gsR < (sR += nums[j]))
                gsR = sR;
        return max(gsL + gsR, max(gs_DC(nums, lo, mi), gs_DC(nums, mi, hi)));
    }
    int maxSubArray(vector<int> &nums)
    {
        int size = nums.size();
        int res = gs_DC(nums, 0, size - 1);
        return res;
    }
};

// greedy algorithm. O(n)
// 从右向左迭代求和，小于 0 则重新计算
class SolutionGR
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int size = nums.size();
        int gs = nums[0], s = 0, i = size;
        while (0 < i--)
        {
            s += nums[i];
            if (gs < s)
                gs = s;
            // Remove negative suffixSum.
            if (s <= 0)
                s = 0;
        }
        return gs;
    }
};

// dynamic programming. O(n)
// 最大子区段取决于（之前的和加上当前值）与（当前值）中的较大者
class SolutionDP
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int size = nums.size();
        int dp = nums[0];
        int gs = dp;
        for (int i = 1; i != size; ++i)
        {
            dp = max(dp + nums[i], nums[i]);
            gs = max(gs, dp);
        }
        return gs;
    }
};

// Driver program to test above
int main()
{
    vector<int> nums{-2, 1, -3, 4, -1, 2, 1, -5, 4};
    SolutionDP sol;
    int res = sol.maxSubArray(nums);
    cout << res;
}