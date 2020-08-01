import math
from typing import List

# ref https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):  # 保证 nums1 更短
            return self.findMedianSortedArrays(nums2, nums1)
        m, n = len(nums1), len(nums2)
        l, r, res = 0, m, -1
        median1, median2 = 0, 0  # 前一部分的最大值，后一部分的最小值

        while l <= r:

            #       left_part          |         right_part
            # A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
            # B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]

            # 前一部分包含 nums1[0 .. i-1] 和 nums2[0 .. j-1]
            # 后一部分包含 nums1[i .. m-1] 和 nums2[j .. n-1]

            i = (l + r) // 2
            j = (m + n + 1) // 2 - i

            # nums_im1, nums_i, nums_jm1, nums_j 分别表示
            # nums1[i-1], nums1[i], nums2[j-1], nums2[j]
            nums_im1 = -math.inf if i == 0 else nums1[i - 1]
            nums_i = math.inf if i == m else nums1[i]
            nums_jm1 = -math.inf if j == 0 else nums2[j - 1]
            nums_j = math.inf if j == n else nums2[j]

            if nums_im1 <= nums_j:
                res = i
                median1, median2 = max(nums_im1, nums_jm1), min(nums_i, nums_j)
                l = i + 1
            else:
                r = i - 1
        return (median1 + median2) / 2 if (m + n) % 2 == 0 else median1  # 分奇偶情况返回


sol = Solution()

nums1 = [1, 3]
nums2 = [2]

print(sol.findMedianSortedArrays(nums1, nums2))
