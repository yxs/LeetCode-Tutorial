import collections


def guessNumber(secret, guess):
    # zip 成 list 中的 tuple, 遍历记录相等的 tuple
    A = sum(s == g for s, g in zip(secret, guess))
    # 计算各自数量，取交集，得到重复元素个数
    B = sum((collections.Counter(secret) & collections.Counter(guess)).values()) - A
    return "{A}A{B}B".format(A=A, B=B)  # int to str
