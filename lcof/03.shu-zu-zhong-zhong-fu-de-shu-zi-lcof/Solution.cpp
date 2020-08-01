// 找出数组中重复的数字。
// 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
// 数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
// 请找出数组中任意一个重复的数字。

// 示例 1：
// ```
// 输入：
// [2, 3, 1, 0, 2, 5, 3]
// 输出：2 或 3
// ```

// 限制：
// 2 <= n <= 100000

// Reference:
// https://github.com/yxs/CodingInterviewChinese2/tree/master/03_01_DuplicationInArray
// https://github.com/yxs/CodingInterviewChinese2/tree/master/03_02_DuplicationInArrayNoEdit
// https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/

#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

// ============ 排序解法：O(nlogn) 时间复杂度，O(1) 空间复杂度 ============
class SolutionSort
{
public:
    int findRepeatNumber(vector<int> &nums)
    {
        // 异常处理
        int res = 0;
        sort(nums.begin(), nums.end());
        for (int i = 0; i != nums.size() - 1; ++i)
        {
            if (nums[i] == nums[i + 1])
            {
                res = nums[i];
                break;
            }
        }
        return res;
    }
};

// ============ 辅助数组/哈希算法：O(n) 时间复杂度，O(n) 空间复杂度 ============
class SolutionHash
{
public:
    int findRepeatNumber(vector<int> &nums)
    {
        unordered_map<int, int> count;
        for (int n : nums)
        {
            if (++count[n] > 1)
                return n;
        }
        return -1;
    }
};

// ============ 二分算法：O(n) 时间复杂度，O(logn) 空间复杂度 ============
class SolutionBinary
{
public:
    int findRepeatNumber(vector<int> &nums)
    {
        if (nums.empty())
            return -1;
        int start = 0;
        int end = nums.size() - 1;
        while (end >= start)
        {
            int mid = ((end - start) >> 1) + start;
            // 统计 start 到 mid 之间的个数
            int count = countRange(nums, start, mid);
            if (end == start)
            {
                if (count > 1)
                    return start;
                else
                    break;
            }
            // 统计前半段
            if (count > (mid - start + 1))
                end = mid;
            // 统计后半段
            else
                start = mid + 1;
        }
        return -1;
    }

    int countRange(vector<int> &nums, int start, int end)
    {
        if (nums.empty())
            return -1;
        int count = 0;
        for (int n : nums)
        {
            if (n >= start && n <= end)
                ++count;
        }
        return count;
    }
};

// ============ 原地置换算法：O(n) 时间复杂度，O(1) 空间复杂度。本解法相较上一个优化了空间复杂度，但代价是修改了数组============
class SolutionExchange
{
public:
    int findRepeatNumber(vector<int> &nums)
    {
        // 异常处理
        if (nums.empty())
            return -1;
        for (int i = 0; i != nums.size(); ++i)
        {
            if (nums[i] < 0 || nums[i] > nums.size() - 1)
                return -1;
        }
        // 一次遍历，通过交换位置，将元素放到其非递减序列下应该处于的位置，如测试用例 0 1 2 2 3 3 5
        for (int i = 0; i != nums.size(); ++i)
        {
            while (nums[i] != i)
            {
                // 重复
                if (nums[i] == nums[nums[i]])
                    return nums[i];
                else
                    // 交换第 0 个 '2' 和 第 2 个 '1'，'2' 就归位了
                    swap(nums[i], nums[nums[i]]);
            }
        }
        return -1;
    }
};

// Driver Code
int main()
{
    vector<int> nums{2, 3, 1, 0, 2, 5, 3};
    SolutionBinary s;
    int res = s.findRepeatNumber(nums);
    cout << res;
    return 0;
}