from typing import List


class Solution:
    # 差分数组
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result = [0] * (n + 1)
        for booking in bookings:
            # start
            result[booking[0] - 1] += booking[2]
            # end
            # mark the end of the range with -seats
            result[booking[1]] -= booking[2]

        # print(result)
        # [10, 45, -10, -20, 0, -25]

        # cumulative sum processing
        tmp = 0
        for i in range(n):
            tmp += result[i]
            result[i] = tmp
        return result[:n]


bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
n = 5
s = Solution()
print(s.corpFlightBookings(bookings, n))
# [10, 55, 45, 25, 25]
