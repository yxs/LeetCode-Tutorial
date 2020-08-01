class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            return False
        d = {}
        for i, n in enumerate(nums):  # 索引序列
            m = target - n
            if m in d:  # 通过哈希表 O(1) 时间查找
                return [d[m], i]
            else:
                d[n] = i  # 存入字典，key 为值，value 为索引


nums = [2, 7, 11, 15]
