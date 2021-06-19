"""
希尔排序：分块的插入排序实现，可以使得排在尾部的较小的数更快的到达前面。
时间复杂度：平均 - O(n^1.3)
空间复杂度：O(1)
稳定性：不稳定
"""
def shell_sort(ls):
    length = len(ls)
    gap = length // 2   # 希尔增量

    while gap >= 1:
        for i in range(gap, length):
            j = i - gap
            flag = ls[i]
            while j >= 0 and ls[j] > flag:
                ls[j+gap] = ls[j]
                j -= gap
            ls[j+gap] = flag
        gap = gap // 2
    return ls


print(shell_sort([2,1,4,3,8,7,6]))