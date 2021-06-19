"""
快速排序：分治的思想，找到标志元素，使得比标识小的位于左侧，大的位于右侧。
时间复杂度：平均 - O(nlogn)   最差 - O(n^2) 标识元素分割为0和n-1   最好 - O(nlogn) 标识元素可以将数组分成两个均衡的部分
空间复杂度：O(logn)
稳定性：不稳定
"""
# 快排的递归方法，移动两个指针
def partition(ls, left, right):
    pivot = ls[left]
    while left < right:
        # 右侧游标往左移动
        while left < right and ls[right] >= pivot:
            right -= 1
        ls[left] = ls[right]
        # 左侧游标往右移动
        while left < right and ls[left] < pivot:
            left += 1
        ls[right] = ls[left]
    ls[left] = pivot
    return left


def quick_sort_recur(ls, start, end):
    if start >= end:
        return

    # 定义两个游标，分别对应开始和结尾
    ind = partition(ls, start, end)

    quick_sort_recur(ls, start, ind-1)
    quick_sort_recur(ls, ind+1, end)


def quick_sort_non_recur(ls):
    if len(ls) < 2:
        return ls
    stack = []
    stack.append(len(ls)-1)
    stack.append(0)
    while stack:
        l = stack.pop()
        r = stack.pop()
        ind = partition(ls, l, r)
        if l < ind-1:
            stack.append(ind-1)
            stack.append(l)
        if r > ind+1:
            stack.append(r)
            stack.append(ind+1)


a = [1, 2, 7, 3, 6, 5]
b = [1, 2, 7, 3, 6, 5]
quick_sort_recur(a, 0, 5)
quick_sort_non_recur(b)
print(a)
print(b)
