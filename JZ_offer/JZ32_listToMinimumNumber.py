"""
Given a list that contains several positive integers, return the minimum number which is a
combination of these separate numbers.
"""

# 直接使用字典序会有问题，没有考虑到整数后面位对排序结果的影响，如[3, 32, 321]，应当自定义组合排序函数
import functools


def comb_compare(a: int, b: int):
    if int(str(a)+str(b)) < int(str(b)+str(a)):
        return -1
    elif int(str(a)+str(b)) > int(str(b)+str(a)):
        return 1
    else:
        return 0


def minimum_number(array: list):
    if len(array) == 0:
        return None
    resort_array = sorted(array, key=functools.cmp_to_key(comb_compare))
    res = ''.join([str(i) for i in resort_array])
    return int(res)


res = minimum_number([3, 32, 321])
print(res)