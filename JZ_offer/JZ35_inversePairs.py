"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对
的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007.题目保证输入的数组中没有的相同的数字
[1,2,3,4,5,6,7,0] ==> 7
"""
import time
import copy


def InversePairs(data):
    # 插入排序实现
    if len(data) < 2:
        return 0
    total = 0
    for i in range(1, len(data)):
        j = i - 1
        tmp = data[i]
        while j >= 0 and data[j] > tmp:
            data[j+1] = data[j]
            total += 1
            j -= 1
        data[j+1] = tmp
    return total % 1000000007


def InversePairs2(data):
    # write code here
    # 排序实现
    if len(data) < 2:
        return 0
    copy_data = copy.deepcopy(data)
    copy_data = sorted(copy_data)
    total = 0
    for i in range(len(copy_data)):
        curr_ind = data.index(copy_data[i])
        total += curr_ind
        data.pop(curr_ind)
    return total


count = 0


def merge_sort(data):
    global count
    if len(data) < 2:
        return data

    mid = len(data) // 2
    ls1 = merge_sort(data[:mid])
    ls2 = merge_sort(data[mid:])

    left, right = 0, 0
    ls = []
    while left < len(ls1) and right < len(ls2):
        if ls1[left] <= ls2[right]:
            ls.append(ls1[left])
            left += 1
        else:
            ls.append(ls2[right])
            count += (len(ls1) - left)
            right += 1
    ls += ls1[left:]
    ls += ls2[right:]
    return ls


def InversePairs3(data):
    merge_sort(data)
    return count

start = time.time()
print(InversePairs([1,2,3,4,5,6,7,0]))
solution1 = time.time()
print(solution1-start)
print(InversePairs2([1,2,3,4,5,6,7,0]))
solution2 = time.time()
print(solution2-solution1)
print(InversePairs3([1,2,3,4,5,6,7,0]))
print(time.time()-solution2)