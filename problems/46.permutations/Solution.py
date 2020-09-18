# 把「路径」和「选择」列表作为决策树上每个节点的属性

def permute(nums):
    def backtrack(first=0):
        if first == n:
            res.append(nums[:])
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)
    res = []
    backtrack()
    return res


nums = [1, 2, 3]
print(permute(nums))
