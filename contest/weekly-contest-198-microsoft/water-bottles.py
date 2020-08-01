class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = numBottles
        while emptyBottles >= numExchange:
            numBottles += emptyBottles // numExchange
            emptyBottles = emptyBottles % numExchange + emptyBottles // numExchange
        return numBottles


sol = Solution()
print(sol.numWaterBottles(15, 4))

