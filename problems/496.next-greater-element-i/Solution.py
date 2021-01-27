class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, d = [], {}
        for n in nums2:
            while stack and stack[-1] < n:
                # pop出的元素为key，下一个更大的元素为v
                d[stack.pop()] = n
            stack.append(n)
        return [d.get(x, -1) for x in nums1]