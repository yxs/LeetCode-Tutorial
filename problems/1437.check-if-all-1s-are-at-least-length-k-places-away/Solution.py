"""
@Date: 2020-05-03 11:27:50
@LastEditors: XueSong Ye
@LastEditTime: 2020-05-03 11:27:51
"""
nums = [1, 0, 0, 1, 0, 1]
k = 2
# nums = [1, 1, 1, 1, 1]
# k = 0
# nums = [0, 1, 0, 1]
# k = 1

index = []
j = flag = 0
for i in range(len(nums)):
    if nums[i] == 1:
        index.append(i)
for i, j in zip(index[:-1], index[1:]):
    if j - i > k:
        pass
    else:
        flag += 1
print(True if flag == 0 else False)
