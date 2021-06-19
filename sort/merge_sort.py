"""
归并排序：归并排序重点在将两个分别有序子数组合并为一个整体的有序数组。
时间复杂度：平均 - O(nlogn)   最差 - O(nlogn)   最好 - O(nlogn)
空间复杂度：O(n)
稳定性：稳定
"""

def merge(ls1, ls2):
    left, right = 0, 0

    ls = []
    while left < len(ls1) and right < len(ls2):
        if ls1[left] <= ls2[right]:
            ls.append(ls1[left])
            left += 1
        else:
            ls.append(ls2[right])
            right += 1
    ls += ls1[left:]
    ls += ls2[right:]
    return ls


def merge_sort(ls):
    if len(ls) < 2:
        return ls
    mid = len(ls) // 2
    ls_left = merge_sort(ls[:mid])
    ls_right = merge_sort(ls[mid:])
    return merge(ls_left, ls_right)


print(merge_sort([2, 3, 1, 8, 9, 5]))