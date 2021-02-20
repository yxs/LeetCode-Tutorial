from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]

        res = []
        for i, char in enumerate(input):
            if char in ["+", "-", "*"]:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1 :])

                for l in left:
                    for r in right:
                        if char == "+":
                            res.append(l + r)
                        elif char == "-":
                            res.append(l - r)
                        else:
                            res.append(l * r)
        return res


input = "2*3-4*5"

s = Solution()
print(s.diffWaysToCompute(input))
# [-34, -14, -10, -10, 10]
