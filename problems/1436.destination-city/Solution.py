"""
@Date: 2020-05-03 10:36:05
@LastEditors: XueSong Ye
@LastEditTime: 2020-05-03 10:57:55
"""

# 由第二个查找第一个

pairs = [["B", "C"], ["D", "B"], ["C", "A"]]

d = dict(pairs)

for v in d.values():
    if v not in list(d.keys()):
        print(v)
