"""
堆排序：
时间复杂度：平均 - O(nlogn)  最差 - O(nlogn)  最好 - O(nlogn)
空间复杂度：O(1)
稳定性：不稳定
"""
def down_compare(ls, start, end):
    # 找到当前节点与待比较的子节点，需要用到列表表示二叉树的下标对应关系
    i , j = start, 2*start+1

    # 循环比较
    while j < end:
        # 先选出子节点中更小的一个，如果只有一个则认为左子节点最小
        if j+1 < end and ls[j+1]<ls[j]:
            j += 1   # 右子节点更小
        if ls[i] >= ls[j]:
            ls[i], ls[j] = ls[j], ls[i]
        else:
            break
        i, j = j, 2 * j + 1
    return ls

def heap_sort(ls: list):
    # 堆初始化,从第一个非叶节点开始，自下而上
    for i in range(len(ls)//2-1, -1, -1):
        ls = down_compare(ls, i, len(ls))
    print(ls)

    # 执行堆排序
    for i in range(len(ls)-1, 0, -1):
        # 交换堆顶与最后一个元素
        ls[i], ls[0] = ls[0], ls[i]
        ls = down_compare(ls, 0, i)
    return ls

res = heap_sort([5,6,8,1,2,4,9])
print(res)
