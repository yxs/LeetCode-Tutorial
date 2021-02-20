class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        base = 1337

        if not b:
            return 1
        last = b.pop()

        p1 = (a ** last) % base
        p2 = (self.superPow(a, b) ** 10) % base

        return (p1 * p2) % base

