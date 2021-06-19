def FindGreatestSumOfSubArray(array):
    # write code here
    max_sum = 0
    curr_sum = 0
    for item in array:
        # 之前的和为负，直接舍弃掉
        if curr_sum < 0:
            curr_sum = item
        else:
            curr_sum += item
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum

# print(FindGreatestSumOfSubArray([1,-2,3,10,-4,7,2,-5]))

def GetNumberOfK(data, k):
    # write code here
    res = 0
    if len(data) == 0:
        return 0
    i, j = 0, len(data)-1
    while i<=j:
        mid = (i + j)//2
        if data[mid] == k:
            for ind1 in range(mid, i-1, -1):
                if data[ind1] == k:
                    res += 1
                else:
                    break
            for ind2 in range(mid+1, j+1):
                if data[ind2] == k:
                    res += 1
                else:
                    break
            return res
        elif data[mid] < k:
            i = mid
        else:
            j = mid
    return res
print(GetNumberOfK([1,2,3,3,3,3,4,5],3))