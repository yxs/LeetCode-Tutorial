"""
@Date: 2020-05-02 23:04:55
@LastEditors: XueSong Ye
@LastEditTime: 2020-05-02 23:23:57
"""

"""
解题思路

1. 从最高位开始调整，有雷同者一并调整，都是改为 9 和 1
2. 若高位已经是 9 or 1，则尝试调整下一位，以此类推
"""
# https://leetcode-cn.com/problems/max-difference-you-can-get-from-changing-an-integer/


class Solution:
    def maxDiff(self, num: int) -> int:

        num_list = list(map(int, str(num)))
        max_num_list = min_num_list = num_list[:]
        j = k = max_flag = min_flag = 0

        for i in num_list:
            if max_flag == 0 and i < 9:
                max_flag = i
                max_num_list[j] = 9
                j += 1
            if i == max_flag:
                max_num_list[j] = 9

            if min_flag == 0 and i > 0:
                min_flag = i
                min_flag = min_num_list[k]
                min_num_list[k] = 1
                k += 1
            if i == min_flag:
                min_num_list[k] = 1

        max_num = int("".join(map(str, max_num_list)))
        min_num = int("".join(map(str, min_num_list)))

        return max_num - min_num


s = Solution()
print(s.maxDiff(123456))
