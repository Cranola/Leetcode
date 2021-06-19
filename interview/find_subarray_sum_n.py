"""
Q1: 给定一个数组，返回和为给定数的连续子数组首尾下标。
A1: 任意连续子数组的和可以看做数组头部到当前元素的和减去数组头部到之前某个元素的和，如在[1, 2, 3, 4, 2]
中，[4,2]的和等于[1, 2, 3, 4, 2]的和减去[1, 2, 3]的和。
"""
def find_substring(ls, n):
    # sum:index
    sum_record = {0: 0}
    curr_sum = 0
    res = []
    for i in range(len(ls)):
        curr_sum += ls[i]
        p = curr_sum - n
        if p in sum_record:
            res.append([sum_record[p], i])
        sum_record[curr_sum] = i+1
    return res

print(find_substring([1, 2, 3, 4, 2], 6))


"""
Q2: 给定一个数组，返回和为给定数的所有数组元素的可能组合，假设数组中元素各不相同。
A2: 讨论当前元素是否在结果序列中的情况，递归求解。
"""
res = []
def find_sum_items(arr: list, curr: list, target: int):
    global res
    # 在中间找到目标值之后，往后继续找加和为0的时候当前序列会重复加入结果中，需要判断是否存在
    # 这样在获取所有可能长度的组合后又不会有重复元素
    if target==0 and curr and curr not in res:
        res.append(curr)
    if not arr:
        return

    find_sum_items(arr[1:], curr, target)
    find_sum_items(arr[1:], curr + [arr[0]], target - arr[0])

def main(arr: list, target: int):
    find_sum_items(arr, [], target)

# main([1,2,3,-1,-2,-3], 0)
# print(res)




