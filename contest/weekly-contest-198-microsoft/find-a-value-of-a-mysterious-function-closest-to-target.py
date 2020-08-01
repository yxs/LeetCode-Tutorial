# ?
class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        ans = abs(arr[0] - target)
        valid = {arr[0]}
        for num in arr:
            valid = {x & num for x in valid} | {num}
            ans = min(ans , min(abs(x - target) for x in valid))
        return ans