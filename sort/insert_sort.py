"""
插入排序：从第2个元素开始，依次与之前的进行比较，当前元素更小则比较元素后移。
时间复杂度：平均 - O(n^2)   最差 - O(n^2) 完全是逆序的时候   最好 - O(n) 顺序的时候
空间复杂度：O(1)
稳定性：稳定
"""
def insert_sort(ls):
    for i in range(1, len(ls)):
        tmp = ls[i]
        j = i - 1
        while j >= 0 and ls[j] > tmp:
            ls[j+1] = ls[j]
            j -= 1
        ls[j+1] = tmp

    return ls


print(insert_sort([2,1,4,3,8,7,6]))