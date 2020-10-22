class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jSet = set(J)
        return sum(s in jSet for s in S)